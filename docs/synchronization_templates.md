# Using the synchronization templates

## Purpose

The MKS synchronization templates use a shared scan schedule instead of independent
periodic scans. This groups frequent and infrequent work on the gauge controller's
serial connection and gives event-scanned records a defined processing order.

The schedule has three parts.

1. [The master database](../vacuumApp/Db/sync_master.db) generates fast, medium, and slow
   EPICS scan events.
2. Records in the MKS synchronization templates subscribe to those event numbers.
3. EPICS processes the subscribed records when their event is generated. Their `PHAS`
   fields provide ordering within an event scan.

Event numbers are identifiers, not time intervals. For example, `fastEvt=1` means
"use EPICS event 1"; it does not mean one second. Scan phases order record processing;
they do not guarantee that asynchronous device communication completes in that order.

## 1. Load the master schedule

Load the installed master database in the consuming input/output controller (IOC)
startup sequence before `iocInit`. Replace `IOC_NAME` with a unique prefix for the IOC.
Select event numbers that do not conflict with other event-driven records in that IOC.

```iocsh
dbLoadRecords("$(VACUUM)/db/sync_master.db", "IOC=IOC_NAME,scanRate=1 second,fastEvt=1,medEvt=2,slowEvt=3")
```

The master database is already installed by this module. `VACUUM` must resolve at runtime
to the selected module release. The master database macros have the following meanings.

| Macro | Meaning |
| --- | --- |
| `IOC` | Prefix for the three master scheduling records |
| `scanRate` | How often the master pacer record runs |
| `fastEvt` | Event number used for frequent gauge operations |
| `medEvt` | Event number used for medium-rate operations |
| `slowEvt` | Event number used for infrequent gauge and controller operations |

The master pacer advances the event sequencer once every four pacer scans. The sequencer
generates 11 fast events, three medium events, and one slow event during each 15-event
cycle. With `scanRate=1 second`, the nominal schedule generates an event every four
seconds, medium events every 20 seconds, and the slow event every 60 seconds. Fast events
occupy the remaining event positions; they are not generated at one fixed period.

These are scheduling intervals, not guarantees of device response time or completed
readbacks. Startup timing and runtime load can affect when processing occurs.

## 2. Subscribe the MKS records

Use the synchronization templates in the consuming IOC's substitutions. Controller
templates require `slowEvt` and `phase`; gauge templates require `fastEvt` and `slowEvt`
in addition to their normal device macros. Match these values to the event numbers
passed to the master database.

The MKS937A templates use those macros as follows.

- Gauge state records use `fastEvt` for frequent status reads.
- Less urgent gauge calculations use `slowEvt`.
- The controller sequence uses `slowEvt` for its longer series of readbacks.
- Gauge templates use `channel` as their scan phase. The controller template uses the
  supplied `phase`. Lower scan phases run before higher phases for the same event.

Choose a controller phase higher than the gauge channel phases when the controller
sequence should start later in the same event scan. The example below uses phase 9,
which is higher than its configured gauge-channel phases.

## 3. Configure substitutions

This MKS937A example uses generic names. Replace the controller and gauge prefixes,
asyn port name, channels, and slots with the configured device values. The asyn port
must be created separately by the consuming IOC.

```text
file sync_mks937a_serial.template
{
    pattern { controller, port, slowEvt, phase }
            { GAUGE_CONTROLLER, GAUGE_PORT, 3, 9 }
}

file sync_mks937a_serial_cc.template
{
    pattern { device, port, channel, slot, fastEvt, slowEvt }
            { COLD_CATHODE_GAUGE, GAUGE_PORT, 1, CC, 1, 3 }
}

file sync_mks937a_serial_pr.template
{
    pattern { device, port, channel, slot, fastEvt, slowEvt }
            { PIRANI_GAUGE, GAUGE_PORT, 4, B1, 1, 3 }
}
```

In this example, event 1 processes the frequent gauge records and event 3 processes the
slow gauge records plus the controller sequence. Gauge channel 1 has phase 1, gauge
channel 4 has phase 4, and the controller sequence has phase 9.

Ensure template lookup resolves to the installed module databases and load the resulting
records before `iocInit`. The relevant source templates are
[the controller template](../vacuumApp/Db/sync_mks937a_serial.template),
[the cold-cathode template](../vacuumApp/Db/sync_mks937a_serial_cc.template), and
[the Pirani template](../vacuumApp/Db/sync_mks937a_serial_pr.template).

## Integration checks

- Confirm that the master and device records load without unresolved macros.
- Confirm that each subscription's event number matches the intended master event.
- Configure protocol lookup and device ports as described in [the README](../README.md).
- Check communication errors and actual update timing on approved test hardware.
  A working event schedule alone does not establish successful device communication.
# Vacuum module architecture

## Purpose and scope

This module provides reusable vacuum database templates, device protocols, and a support
library for consuming IOCs. The migration preserves the R0.1.2 device interface while
targeting Rocky Linux 9 and EPICS 7.

This repository is not a configured standalone IOC. It has no child IOC startup files
or device endpoint configuration.

## Components

| Component | Responsibility |
| --- | --- |
| [Database sources](../vacuumApp/Db) | MKS gauge, Gamma pump, Varian turbo, cryo-ready, and synchronization records |
| [Protocol sources](../vacuumApp/protocols) | StreamDevice communication definitions used by the database templates |
| [Support build](../vacuumApp/src/Makefile) | Builds the `vacuum` library and combined database definition |
| [Dependency configuration](../configure/RELEASE.local) | Selects support-module releases and defines EPICS Base last |
| [Target configuration](../configure/CONFIG_SITE) | Clears cross-target selection so the build uses the host target |

The support build combines Base, IOC administration, autosave, asyn, StreamDevice, and
modbus database definitions. It links their support libraries, including ModBusTCPClnt.
It builds a library rather than an IOC executable; `PROD_IOC` is commented out.

The [database Makefile](../vacuumApp/Db/Makefile) installs the selected templates and
databases, including IOC administration and autosave status databases from dependencies.

## Runtime integration

The consuming IOC supplies the executable, startup sequence, device ports, database
macro values, and protocol search path. Its records use the support registered by the
combined database definition. StreamDevice records refer to protocol files by name.

Protocol files remain under `vacuumApp/protocols`. The application build does not
traverse that directory. No protocol-copy change is planned solely for this migration.
Deployment must retain the protocol sources, and the consuming IOC must make them
available through `STREAM_PROTOCOL_PATH`. The actual consumer setup remains unverified.

## Design boundaries

- Preserve existing process variable (PV) names, macros, device commands, and alarms.
- Keep deployment-specific addresses and startup configuration in the consuming IOC.
- Do not introduce new records or change protocol behavior as migration cleanup.
- Treat configured dependencies and source review as distinct from build and hardware
  acceptance. Current validation gaps are in [implementation status](implementation_status.md).
# Vacuum module requirements

## Rocky Linux 9 Migration scope

Make the R0.1.2-based vacuum module usable by its consuming IOC on Rocky 9 with
EPICS 7. This is a compatibility migration, not a device-interface redesign.

This creates a new branch R0.1.2-rocky9.

Rocky 9 is the requested target. Support for RHEL 7 and older Red Hat operating systems
is outside the scope of this version.

## Compatibility

- Preserve existing process variable (PV) names, template macros, units, alarm settings,
  and device-command behavior unless a separate requirement approves a change.
- Use mutually compatible EPICS Base and support-module releases with libraries for
  `rhel9-x86_64`. Dependency-directory checks alone do not establish target availability.
- Keep the library and database-definition interface usable by the consuming IOC.
- Preserve database and protocol filenames referenced by existing consumers.
- Avoid adding unrelated support modules or speculative linker dependencies.

## Consumer and deployment integration

- Install the databases declared in the [database Makefile](../vacuumApp/Db/Makefile).
- Retain the protocol source directory in the deployed release and configure the
  consuming IOC's `STREAM_PROTOCOL_PATH` to find its files.
- Resolve required shared libraries on the runtime host, not just the build host.

## Safety and acceptance

- Use approved test hardware or an established simulator for functional testing.
- Avoid duplicate PVs and competing connections to equipment during migration tests.
- Perform device writes, resets, and other state-changing tests only when approved.
- Verify database loading, support registration, macro expansion, and protocol lookup
  before interpreting hardware communication failures.
- Verify required readings, approved commands, alarms, communication failure and
  recovery, restart behavior, and autosave integration in the consuming IOC.
- Do not claim hardware or safety acceptance from source inspection or a successful
  build alone. Device behavior has not been checked against original vendor references
  in this documentation.
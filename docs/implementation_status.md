# Vacuum module implementation status

## Current state

The R0.1.2-based migration is configured for Rocky Linux 9 and EPICS 7. The items below
describe the inspected working tree, not a tested or released deployment.

Migration configuration and documentation were restored on 2026-10-08 after the working
tree returned to the EPICS 3.14 baseline. Device records and protocol sources were not
changed during restoration.

## Implemented configuration changes

- [Dependency checks](../configure/RELEASE) cover only the declared support modules
  and use `STREAMDEVICE` consistently with the dependency configuration.
- [Site configuration](../RELEASE_SITE) selects EPICS Base `R7.0.3.1-2.0` and its module
  tree. [RELEASE.local](../configure/RELEASE.local) defines Base last.
- [Target configuration](../configure/CONFIG_SITE) clears `CROSS_COMPILER_TARGET_ARCHS`
  and no longer assigns an architecture list to `BUILD_FOR_HOST_ARCH`.
- [Support registration](../vacuumApp/src/Makefile) uses `asSupport.dbd` for autosave
  and retains `stream.dbd` for StreamDevice.
- [README](../README.md) describes module purpose and consumer integration without the
  obsolete version-variable example.
- [Ignore rules](../.gitignore) exclude generated outputs and untracked site configuration.
  `RELEASE_SITE` is currently tracked; the ignore rule does not untrack an existing file.

## Selected dependencies

The following releases are selected in [RELEASE.local](../configure/RELEASE.local).
Earlier filesystem inspection found `rhel9-x86_64` libraries for all six releases.
Artifact presence does not establish a successful module build or runtime acceptance.

| Dependency | Selected release |
| --- | --- |
| asyn | `R4.42-1.0.0` |
| autosave | `R5.11-2.1.1` |
| iocAdmin | `R3.1.16-1.4.0` |
| ModBusTCPClnt | `R2.3.0-1.2.1` |
| modbus | `R3.2-1.0.3` |
| StreamDevice | `R2.8.9-1.3.2` |

## Pending verification

- Successful Rocky9 build and review of build warnings.
- Consuming IOC dependency selections, database-definition integration, and startup.
- Deployed protocol-directory availability and the actual `STREAM_PROTOCOL_PATH`.
- Runtime shared-library resolution, including StreamDevice's PCRE dependency.
  `PROD_SYS_LIBS_DEFAULT += pcre` remains in the library Makefile; this executable-only
  setting does not itself add PCRE to the shared-library link.
- Hardware readings, approved commands, alarms, communication recovery, restart, and
  autosave behavior. No hardware acceptance evidence has been provided.

RHEL7 testing is outside the documented scope. No builds, IOC launches, device writes,
or deployment actions were performed during restoration. Protocol packaging is unchanged
pending consumer-path verification.
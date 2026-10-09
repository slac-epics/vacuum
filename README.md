## Vacuum support module

Reusable vacuum database templates, StreamDevice protocols, and a support library for
LCLS vacuum IOCs. The module contains support for MKS gauges, Gamma pumps, Varian turbo pumps, cryo-ready records, and gauge synchronization.

This is not a standalone IOC. The consuming IOC provides the executable, startup configuration, device connections, and record macros.

### Platform

This version targets Rocky Linux 9 and EPICS 7 using the `rhel9-x86_64` architecture.
RHEL7 and older Red Hat platforms are outside its supported scope. Existing process
variable (PV) names, template macros, and device interfaces are retained.

### Documentation

- [Architecture](docs/architecture.md) describes components and runtime integration.
- [Requirements](docs/requirements.md) defines compatibility and acceptance requirements.
- [Implementation status](docs/implementation_status.md) records dependency selections,
  migration progress, and outstanding build and hardware validation.
- [Synchronization templates](docs/synchronization_templates.md) explain the shared scan schedule, required macros, and MKS937A substitution examples.

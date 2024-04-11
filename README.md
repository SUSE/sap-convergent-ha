# sap-convergent-ha

Resource agent to control the Convergent Mediation control zone components


## Introduction

SAPCMControlZone is a resource agent for managing the Convergent Mediation (CM)
ControlZone platform and UI for a single instance as HA resources.

The CM entral ControlZone platform is responsible for providing services to
other instances. Several platform containers may exist in a CM system, for high
availability, but only one is active at a time. The CM central ControlZone UI
is used to query, edit, import, and export data. This ControlZone services can
be handled as active/passive resources.
Currently supported services are "platform" and "ui".

NFS shares with work directories can be mounted statically on all nodes. The HA
cluster does not need to control that filesystems.

The resource agent uses the mzsh as interface provided by the ControlZone.
Please see also the REQUIREMENTS section in manual page
ocf_suse-SAPCMControlZone(7).


## License

See the [LICENSE](LICENSE) file for license rights and limitations.


## Feedback
Do you have suggestions for improvement? Let us know!

Go to Issues, create a [new issue](https://github.com/SUSE/sap-convergent-ha/issues)
and describe what you think could be improved.

Feedback is always welcome!


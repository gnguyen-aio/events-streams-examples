ARG IGNITION_VERSION=latest
FROM inductiveautomation/ignition:${IGNITION_VERSION}

# If you have additional modules, copy them into the user-lib/modules folder
COPY --chown=ignition:ignition ./external-modules/MQTT-Distributor-signed.modl /usr/local/bin/ignition/user-lib/modules/
COPY --chown=ignition:ignition ./external-modules/MQTT-Engine-signed.modl /usr/local/bin/ignition/user-lib/modules/
COPY --chown=ignition:ignition ./external-modules/MQTT-Transmission-signed.modl /usr/local/bin/ignition/user-lib/modules/
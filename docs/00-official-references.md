# Official references — CSW Ingest appliance & Ingest connectors

> Always defer to these authoritative Cisco sources over any community guide.

## Secure Workload core

| Topic | Link |
|---|---|
| Secure Workload product docs (all versions) | <https://www.cisco.com/c/en/us/support/security/tetration/series.html> |
| Configure and Manage Connectors (4.0) | <https://www.cisco.com/c/en/us/td/docs/security/workload_security/secure_workload/user-guide/4_0/cisco-secure-workload-user-guide-saas-v40/m-connectors.html> |
| Compatibility Matrix | <https://www.cisco.com/c/m/en_us/products/security/secure-workload-compatibility-matrix.html> |
| Deployment / landing page | <https://www.cisco.com/c/en/us/td/docs/security/workload_security/secure_workload/landing-page/secureworkload-40-docs.html> |
| Upgrade Guide (appliance redeploy) | <https://www.cisco.com/c/en/us/support/security/tetration/products-installation-guides-list.html> |

## Virtual appliances

- **Secure Workload Ingest:** 8 vCPU · 8 GB RAM · 250 GB · **3 NICs** · up to **3 connectors** · up to **100 per root scope**. Connectors **listen on ports** (slot-based).
- **Secure Workload Edge:** 8 vCPU · 8 GB RAM · 250 GB · **1 NIC** · up to **8 connectors** · **one per root scope**. (See [csw-edge-connector](https://github.com/chandrapati/csw-edge-connector).)
- OS bundled in OVA/QCOW2: AlmaLinux 9.2 (CSW 3.8.1.36+) / CentOS 7.9 (earlier).

## Ingest connectors & default ports

| Connector | Protocol | Default port |
|---|---|---|
| NetFlow | NetFlow v9 | UDP 4729 |
| Secure Firewall (ASA/FTD) | NSEL (NetFlow) | UDP 4729 (example) |
| Meraki | NetFlow | UDP 4729 |
| F5 | IPFIX | UDP 4739 |
| NetScaler | AppFlow (IPFIX) | UDP 4739 |
| AnyConnect | IPFIX / nvzFlow | UDP 4739 |
| ERSPAN | ERSPAN (GRE) | IP proto 47 (3 connectors auto) |

> Listening ports can be changed on the connector container via the appliance `update-listening-ports` allowed command (needs the connector ID from the connector page).

## Related integration guides

- Edge appliance: <https://github.com/chandrapati/csw-edge-connector>
- Secure Connector (SaaS tunnel): <https://github.com/chandrapati/csw-secure-connector>
- AnyConnect NVM: <https://github.com/chandrapati/csw-anyconnect-nvm>
- F5: <https://github.com/chandrapati/csw-f5-integration> · NetScaler: <https://github.com/chandrapati/csw-netscaler-integration>
- User Education hub: <https://github.com/chandrapati/CSW-User-Education>

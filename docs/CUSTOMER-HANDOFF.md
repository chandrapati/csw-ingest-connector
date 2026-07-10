# Customer handoff — CSW Ingest appliance deployment checklist

Use this as the closeout artifact for an Ingest appliance engagement. Anonymize all customer identifiers.

## 1. Scope & goals

- [ ] Root scope + which flow sources to ingest agreed (NetFlow / F5 / NetScaler / ASA-NSEL / Meraki / AnyConnect / ERSPAN).
- [ ] Number of connectors mapped to appliances (≤ 3 per appliance; add appliances to scale, ≤ 100/root scope).
- [ ] For ERSPAN: target VLAN/port list scoped to avoid packet drops.

## 2. Prerequisites verified

- [ ] ESXi/KVM host has **8 vCPU / 8192 MB / 250 GB** reservable.
- [ ] **3 NICs / slot IPs** planned (one per connector as needed).
- [ ] Exporter → connector reachability on the right ports (UDP **4729** / **4739**) or GRE path for ERSPAN.
- [ ] Outbound **TLS** appliance → CSW cluster confirmed (or Secure Connector planned).
- [ ] **NTP** and **DNS** reachable.

## 3. Deploy

- [ ] Ingest VM deployed from current OVA/QCOW2 with config bundle attached.
- [ ] Appliance **Active** in **Manage → Virtual Appliances**; CPU/Mem/Disk < 90%.
- [ ] (ERSPAN) 3 ERSPAN connectors auto-provisioned.

## 4. Configure exporters

- [ ] Each device's NetFlow/IPFIX/AppFlow collector set to the connector **slot IP:port**.
- [ ] (ERSPAN) switch SPAN/ERSPAN source session pointed at connector interface.
- [ ] Any port changes done via `update-listening-ports` recorded.

## 5. Validate

- [ ] Connector heartbeats green with non-zero received records.
- [ ] Flows visible in **Investigate → Flows** for each exporter (screenshot captured).
- [ ] NAT stitching verified for F5 / NetScaler / ASA.
- [ ] ERSPAN **Agent Packet Misses** ~0.

## 6. Handoff

- [ ] Day-2 owners named for appliance health, slot/port map, and exporter configs.
- [ ] Slot/IP/port inventory documented per appliance.
- [ ] Redeploy-to-patch process documented (no in-place OS patching).
- [ ] Guide + architecture diagram shared; links to Edge and Secure Connector repos provided.

---

*Community reference checklist · Cisco Solutions Engineering · anonymized, no customer data.*

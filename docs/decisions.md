# Decision Journal

A running log of the non-obvious choices I made and why. Newest first. This is gold in interviews — hiring managers care about *why*, not just *what*.

Format: one entry per decision.

---

## YYYY-MM-DD — <short title>

**Context.** What was the situation / constraint?

**Options.** What did I consider?

**Decision.** What did I choose?

**Why.** The trade-off I made and what I gave up.

**Revisit if.** What would make me change this later?

---

<!-- Example (delete once you have real entries):

## 2026-03-14 — Partition orders by order_date, cluster by customer_id

**Context.** Gold `fct_orders` was scanning the whole table on common date-range queries.
**Options.** No partitioning; partition by ingestion time; partition by order_date.
**Decision.** Partition by `order_date`, cluster by `customer_id`.
**Why.** Analysts filter by date almost every query, so partition pruning cuts bytes scanned (and cost) the most; clustering on customer_id speeds the next-most-common filter. Ingestion-time partitioning wouldn't help date-range queries.
**Revisit if.** Query patterns shift to customer-first access, or the table grows past the point where clustering alone is enough.
-->

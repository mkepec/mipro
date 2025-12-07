# Master Index: All Paper Proposals

**Last Updated**: 2025-12-07
**Total Proposals**: 10 ideas across 3 categories
**Status Legend**:
- 🟢 READY - Feasible, well-defined, can start immediately
- 🟡 NEEDS VALIDATION - Requires technical validation before proceeding
- 🔴 FUTURE - Long-term idea, not ready for immediate work
- ⚪ ON HOLD - Interesting but lower priority

---

## Quick Reference Table

| ID | Title | Conference | Status | Priority | Timeline | File |
|----|-------|------------|--------|----------|----------|------|
| **EDUCATION TRACK** |
| E1 | IaC Progressive Learning (Learner Lab) | CE/EE | 🟡 | **HIGH** | MIPRO 2027 | `paper_e1_iac_progressive_learning_learner_lab.md` |
| E2 | MCP Infrastructure Assessment (Teacher) | CE | 🟡 | **MED-HIGH** | MIPRO 2027 | `paper_e2_mcp_infrastructure_assessment_teacher.md` |
| E3 | Cloud-Native Classroom (IaC + K8s Labs) | CE/EE | 🟢 | MEDIUM | MIPRO 2027 | `paper_e3_d2_s1_phase4_proposals.md` #1 |
| E4 | MCP for Programming Assessment | CE | 🔴 | LOW | Future | `../brainstorming/education_iac_mcp_ideas.md` #2 |
| E5 | MCP Tutorial Paper | SSE | ⚪ | LOW | Future | `../brainstorming/education_iac_mcp_ideas.md` #3 |
| **DEVOPS / OBSERVABILITY TRACK** |
| D1 | MCP for Observability & Incident Response | SSE/AIS | 🟢 | **HIGH** | MIPRO 2027 | `paper_d1_mcp_observability_incident_response.md` |
| D2 | Self-Healing System (LLM RCA) | AIS/SSE | 🟢 | **HIGH** | MIPRO 2027 | `paper_e3_d2_s1_phase4_proposals.md` #2 |
| D3 | Centralized Logging with ADX | SSE | 🟢 | MEDIUM | MIPRO 2027 | `paper_d3_d4_devops_logging_ideas.md` #1 |
| D4 | High-Throughput Log Shipper Optimization | SSE | 🟢 | MEDIUM | MIPRO 2027 | `paper_d3_d4_devops_logging_ideas.md` #2 |
| **SPECIAL PROJECTS** |
| S1 | University Digital Twin | CE/EE/CIS | 🔴 | LOW | MIPRO 2028+ | `paper_e3_d2_s1_phase4_proposals.md` #3 |

---

## PRIORITY 1: HIGH-IMPACT, NEAR-TERM (Ready for MIPRO 2026-2027)

### 🎯 E1: IaC Progressive Learning in AWS Academy Learner Lab

**Status**: 🟡 NEEDS VALIDATION (Terraform/CloudFormation feasibility)
**Priority**: ⭐⭐⭐⭐⭐ **HIGHEST** (You teach this, real problem, novel)
**Timeline**: Validate by Oct 2025 → Pilot Spring 2026 → MIPRO 2027
**Conference**: CE (Computers in Education) or EE (Engineering Education)

**Core Idea**:
- Use IaC (Terraform/CloudFormation) for weekly lab prerequisites
- Ensure students start each lab with correct infrastructure
- Create skill-based assessments with intentionally broken infrastructure

**What Makes It Strong**:
- ✅ Novel: No one has done IaC for progressive learning in AWS Academy
- ✅ Practical: Solves YOUR real teaching pain point
- ✅ Feasible: You have students, course, and data
- ✅ Publishable: Great fit for CE/EE
- ✅ Open-source: Reusable Terraform modules for community

**Critical Blocker**:
- ❓ Can Terraform/CloudFormation run in AWS Academy Learner Lab?
- ❓ Do temporary credentials work with IaC state management?

**Next Action**:
- [ ] **VALIDATE THIS WEEK**: Test Terraform in Learner Lab CloudShell
- [ ] Test CloudFormation stack creation
- [ ] Document findings and make GO/NO-GO decision

**File**: `paper_e1_iac_progressive_learning_learner_lab.md`

---

### 🎯 D1: MCP for Observability & LLM-Driven Incident Response

**Status**: 🟢 READY (Can start prototyping immediately)
**Priority**: ⭐⭐⭐⭐⭐ **HIGHEST** (Intersects DevOps + AI expertise)
**Timeline**: Prototype Oct-Dec 2025 → Pilot Jan-Jun 2026 → MIPRO 2027
**Conference**: SSE (Software and Systems Engineering) or AIS

**Core Idea**:
- Build MCP servers for Prometheus, ADX/Elasticsearch, Jaeger
- Enable LLMs to query observability data during incidents
- Measure MTTR reduction vs traditional manual investigation

**What Makes It Strong**:
- ✅ Novel: First MCP application in enterprise observability
- ✅ Expertise: Perfect alignment with your Infobip work (ADX, observability)
- ✅ Practical: Real production deployment possible
- ✅ Data: Historical incident data available
- ✅ Impact: High industry relevance

**No Blockers**:
- ✓ MCP is proven technology
- ✓ You have observability platforms at work
- ✓ Incident data exists

**Next Action**:
- [ ] Build prototype Prometheus MCP server (2 weeks)
- [ ] Build prototype ADX MCP server (2 weeks)
- [ ] Test with historical incident from last 6 months
- [ ] Compare LLM+MCP analysis to actual post-mortem

**Combines Well With**: D2 (Self-Healing System) - can merge these!

**File**: `paper_d1_mcp_observability_incident_response.md`

---

### 🎯 D2: Self-Healing System (LLM Fine-Tuning for RCA)

**Status**: 🟢 READY (From Phase 4, well-defined)
**Priority**: ⭐⭐⭐⭐ HIGH
**Timeline**: MIPRO 2027
**Conference**: AIS (Artificial Intelligence Systems) or SSE

**Core Idea**:
- Fine-tune LLM on historical observability data
- Generate root cause analysis hypotheses
- Compare accuracy to traditional alert correlation

**What Makes It Strong**:
- ✅ AI/ML focus (hot topic for AIS)
- ✅ XAI component (explainable AI)
- ✅ Addresses real AIOps challenge
- ✅ Industry impact

**Can Combine With D1**:
- D1 provides MCP architecture (how to connect LLM to data)
- D2 provides intelligence (fine-tuned model)
- Together: Complete solution

**Next Action**:
- [ ] Consider merging with D1 (MCP Observability)
- [ ] Combined paper title: "LLM-Enhanced Root Cause Analysis with Model Context Protocol"

**File**: `paper_e3_d2_s1_phase4_proposals.md` (Proposal #2)

---

### 🔍 E2: MCP for AWS Infrastructure Assessment (Teacher Tool)

**Status**: 🟡 NEEDS VALIDATION (Teacher access to student accounts?)
**Priority**: ⭐⭐⭐ MEDIUM-HIGH
**Timeline**: Validate Oct 2025 → If viable, MIPRO 2027
**Conference**: CE (Computers in Education)

**Core Idea**:
- MCP server that lets teachers use LLMs to grade student AWS infrastructure
- Similar to AWS Academy guided lab grading scripts, but for Learner Lab
- Parallel to Paper 08 (LLM Database Assessment)

**What Makes It Strong**:
- ✅ Novel: MCP for infrastructure assessment
- ✅ Inspired by Paper 08 (proven concept for CE)
- ✅ Addresses real problem (teacher grading time)
- ✅ AI/LLM application in education

**Critical Blocker**:
- ❓ Can teachers programmatically access student AWS accounts?
- ❓ Learner Lab only provides GUI access, not API credentials?

**Next Action**:
- [ ] **VALIDATE WEEK 2**: Check if AWS Academy provides API for teacher access
- [ ] Email AWS Academy support
- [ ] If NO access → Pivot to student self-assessment tool
- [ ] If YES → Build prototype MCP server

**Pivot Options if Not Viable**:
- Student-facing tool (they check their own work before submission)
- Screenshot-based assessment (teacher uploads screenshots to LLM)
- Focus on guided lab enhancement instead

**File**: `paper_e2_mcp_infrastructure_assessment_teacher.md`

---

## PRIORITY 2: SOLID IDEAS, LONGER TIMELINE

### E3: Cloud-Native Classroom (IaC + Kubernetes Labs)

**Status**: 🟢 READY (Well-defined from Phase 4)
**Priority**: ⭐⭐⭐ MEDIUM
**Timeline**: MIPRO 2027-2028
**Conference**: CE/EE

**Core Idea**:
- IaC framework (Terraform + Kubernetes) for "Lab-as-Code"
- Containerized lab environments for DevOps topics
- Comparative study: IaC labs vs traditional VM labs

**What Makes It Strong**:
- ✅ Novel framework
- ✅ Open-source contribution
- ✅ Industry-relevant (teaches real tools)

**Why Not Priority 1**:
- Broader scope than E1 (Learner Lab)
- Requires more infrastructure setup
- Less directly tied to AWS Academy

**Relationship to E1**:
- E1 is AWS-specific (Learner Lab)
- E3 is generic (Kubernetes, any cloud)
- Could do E1 first, then generalize to E3

**File**: `paper_e3_d2_s1_phase4_proposals.md` (Proposal #1)

---

### D3: Centralized Logging with Azure Data Explorer

**Status**: 🟢 READY (Based on your real Infobip work)
**Priority**: ⭐⭐⭐ MEDIUM
**Timeline**: MIPRO 2027
**Conference**: SSE

**Core Idea**:
- Architectural case study: Vector → Event Hubs → ADX
- Performance comparison: ADX vs ELK stack
- Analysis of 200+ Graylog cluster migration

**What Makes It Strong**:
- ✅ Real production data (your Infobip migration)
- ✅ Practical case study
- ✅ Performance benchmarks
- ✅ Cost analysis

**Why Not Priority 1**:
- More case study than research
- Less novelty than MCP papers
- But still publishable!

**Next Action**:
- [ ] Collect migration metrics from Infobip
- [ ] Anonymize data
- [ ] Document architecture diagrams
- [ ] Write as case study paper

**File**: `paper_d3_d4_devops_logging_ideas.md` (Topic #1)

---

### D4: High-Throughput Log Shipper Optimization

**Status**: 🟢 READY (Practitioner-focused)
**Priority**: ⭐⭐ MEDIUM
**Timeline**: MIPRO 2027
**Conference**: SSE

**Core Idea**:
- Kernel tuning for log shippers (sysctl, NIC buffers)
- Comparative analysis: Vector vs Fluent-bit vs Logstash
- Best practices guide for handling log spikes

**What Makes It Strong**:
- ✅ Practical "how-to" paper
- ✅ Benchmark-driven
- ✅ Industry pain point

**Why Not Priority 1**:
- More tutorial/practice than research
- Narrower audience
- Better for practitioner journals (IEEE Software)

**Next Action**:
- [ ] Run benchmarks at Infobip
- [ ] Document tuning parameters
- [ ] Create reproducible test setup

**File**: `paper_d3_d4_devops_logging_ideas.md` (Topic #2)

---

## PRIORITY 3: FUTURE / LOWER PRIORITY

### E4: MCP for Programming Assessment (General)

**Status**: 🔴 FUTURE
**Priority**: ⭐ LOW
**Conference**: CE

**Core Idea**:
- MCP server for grading programming assignments
- Dual mode: teacher grading + student hints
- More generic than E2 (not AWS-specific)

**Why Lower Priority**:
- Overlaps with E2 (similar concept)
- Broader scope (all programming, not just AWS)
- Requires more implementation
- E2 (AWS-specific) is more feasible first paper

**Relationship to E2**:
- E2 is specialized (AWS infrastructure)
- E4 is generalized (any programming)
- Do E2 first, then generalize to E4 later

**File**: `education_iac_mcp_ideas.md` (Idea #2)

---

### E5: MCP Tutorial Paper

**Status**: ⚪ ON HOLD (Not right format for MIPRO)
**Priority**: ⭐ LOW for MIPRO, HIGH for blog/workshop
**Conference**: SSE (but better as blog post)

**Core Idea**:
- Comprehensive guide to building MCP servers
- Design patterns and best practices
- Integration examples

**Why Not MIPRO**:
- Tutorial format, not research
- Better for practitioner venues
- Consider: blog post series, GitHub repo, workshop

**Alternative Venues**:
- IEEE Software magazine
- ACM Queue
- Medium blog series
- YouTube tutorial series

**File**: `education_iac_mcp_ideas.md` (Idea #3)

---

### S1: University Digital Twin

**Status**: 🔴 FUTURE (Long-term project)
**Priority**: ⭐ LOW
**Timeline**: MIPRO 2028+
**Conference**: CE/EE/CIS

**Core Idea**:
- Digital Twin of university IT infrastructure
- Sandbox for cybersecurity education
- High-fidelity training environment

**Why Lower Priority**:
- Very large scope
- Requires institutional support
- Multi-year project
- Better as PhD thesis or grant-funded research

**Recommendation**:
- Don't pursue for MIPRO 2026-2027
- Consider for future grant application
- Or multi-paper series over 3-5 years

**File**: `paper_e3_d2_s1_phase4_proposals.md` (Proposal #3)

---

## Recommended Action Plan

### IMMEDIATE (October 2025) - VALIDATION PHASE

**Week 1-2: Critical Validations**
```
[ ] E1: Test Terraform/CloudFormation in AWS Learner Lab
    - Can it run? Does state management work?
    - GO/NO-GO decision

[ ] E2: Contact AWS Academy about programmatic student account access
    - Email support, check documentation
    - GO/NO-GO decision

[ ] D1: Build MCP prototype for Prometheus
    - Prove concept works
    - Test with historical incident
```

**Week 3-4: Decision Point**
```
Based on validation results:

IF E1 is viable:
  → Focus on E1 as PRIMARY paper (highest priority)
  → Target MIPRO 2027
  → You teach it, can pilot Spring 2026

IF E1 is NOT viable:
  → Focus on D1 (MCP Observability) as PRIMARY
  → Also strong, no blockers
  → Target MIPRO 2027

IF E2 is viable:
  → Secondary paper project
  → Start alongside primary

IF E2 is NOT viable:
  → Pivot to student self-assessment version
```

---

### NEAR-TERM (Nov 2025 - Mar 2026) - PILOT PHASE

**Option A: E1 is Primary**
```
Nov-Dec 2025: Develop IaC modules for 4-6 weeks
Jan-May 2026: Pilot with Spring AWS Academy course
Jun-Aug 2026: Analyze data
Sep-Oct 2026: Write paper
Jan 2027: Submit to MIPRO 2027
```

**Option B: D1 is Primary**
```
Nov-Dec 2025: Build production MCP servers (Prometheus, ADX, Jaeger)
Jan-Feb 2026: Deploy at Infobip, train team
Mar-Jun 2026: Collect incident data, MTTR metrics
Jul-Sep 2026: Analysis & paper writing
Jan 2027: Submit to MIPRO 2027
```

---

### MEDIUM-TERM (2026-2027) - SECONDARY PAPERS

**Once primary paper is done:**
1. Pursue secondary idea (E2 or D2)
2. Consider merging D1 + D2 into comprehensive paper
3. Write up D3 (ADX migration case study)
4. Consider D4 for practitioner venue

---

## Key Decision Points

### Decision 1: E1 Viability (End of October 2025)
**Question**: Can IaC work in AWS Learner Lab?
**Impact**: Determines if E1 is viable as primary paper
**Action**: Technical validation testing

### Decision 2: E2 Viability (End of October 2025)
**Question**: Can teachers programmatically access student AWS accounts?
**Impact**: Determines if E2 is viable or needs pivot
**Action**: AWS Academy support inquiry

### Decision 3: Timeline Choice (November 2025)
**Question**: Target MIPRO 2026 or 2027?
**Impact**: Determines project pace and scope
**Recommendation**: MIPRO 2027 (more realistic for thorough research)

---

## Conference Fit Summary

### CE (Computers in Education)
- E1: IaC Progressive Learning ⭐⭐⭐⭐⭐
- E2: MCP Infrastructure Assessment ⭐⭐⭐⭐
- E3: Cloud-Native Classroom ⭐⭐⭐⭐
- E4: MCP Programming Assessment ⭐⭐⭐

### SSE (Software and Systems Engineering)
- D1: MCP Observability ⭐⭐⭐⭐⭐
- D2: Self-Healing System ⭐⭐⭐⭐
- D3: Centralized Logging ⭐⭐⭐⭐
- D4: Log Shipper Optimization ⭐⭐⭐

### AIS (Artificial Intelligence Systems)
- D2: Self-Healing System ⭐⭐⭐⭐⭐
- D1: MCP Observability ⭐⭐⭐⭐

### EE (Engineering Education)
- E1: IaC Progressive Learning ⭐⭐⭐⭐
- E3: Cloud-Native Classroom ⭐⭐⭐⭐

---

## Summary Statistics

**Total Ideas**: 10 proposals
**Ready to Start**: 5 papers (E3, D1, D2, D3, D4)
**Needs Validation**: 2 papers (E1, E2)
**Future/Low Priority**: 3 papers (E4, E5, S1)

**By Conference**:
- CE/EE: 6 papers
- SSE: 5 papers
- AIS: 2 papers

**By Expertise Alignment**:
- DevOps/Observability: 4 papers (D1, D2, D3, D4)
- AWS/Cloud Education: 4 papers (E1, E2, E3, E4)
- Hybrid (DevOps + Education): 2 papers (E1, E3)

---

## Final Recommendations

### For MIPRO 2027 (January 2027 Submission)

**Primary Paper Choice**:
1. **E1 (IaC Progressive Learning)** - IF validation succeeds
   - Highest novelty + feasibility combination
   - You have students and course
   - Real problem with practical solution

2. **D1 (MCP Observability)** - IF E1 validation fails OR as second paper
   - No technical blockers
   - Perfect expertise match
   - High industry impact

**Secondary Paper** (if time allows):
- E2 (MCP Assessment) - IF validation succeeds
- D2 (Self-Healing) - Can merge with D1
- D3 (ADX Case Study) - Lower effort, good backup

### Next Steps This Week

1. **Validate E1**: Test IaC in Learner Lab ← CRITICAL
2. **Validate E2**: Email AWS Academy support
3. **Prototype D1**: Build basic MCP for Prometheus
4. **Make Decision**: End of October, choose primary paper

---

**Last Updated**: 2025-12-07
**Owner**: Marin Kepec
**Target**: MIPRO 2027 (SSE or CE track)

# Research Proposals Directory

**Last Updated**: 2025-12-07

This directory contains all concrete paper proposals for MIPRO conference submissions.

---

## Directory Structure

### Master Index
- **`MASTER_PAPER_INDEX.md`** - Complete overview of all 10 paper proposals with priorities, timelines, and recommendations

### Individual Proposal Files

**Education Track (E):**
- `paper_e1_iac_progressive_learning_learner_lab.md` - IaC for AWS Academy Learner Lab (HIGH PRIORITY)
- `paper_e2_mcp_infrastructure_assessment_teacher.md` - MCP for grading student AWS work (MED-HIGH)
- `paper_e3_d2_s1_phase4_proposals.md` - Phase 4 proposals:
  - E3: Cloud-Native Classroom
  - D2: Self-Healing System (LLM RCA)
  - S1: University Digital Twin

**DevOps / Observability Track (D):**
- `paper_d1_mcp_observability_incident_response.md` - MCP for incident response (HIGH PRIORITY)
- `paper_d3_d4_devops_logging_ideas.md` - Contains:
  - D3: Centralized Logging with ADX
  - D4: High-Throughput Log Shipper Optimization

---

## Naming Convention

**Format**: `paper_<ID>_<descriptive_name>.md`

**ID Prefixes**:
- **E1-E5**: Education papers (CE/EE conferences)
- **D1-D4**: DevOps/Observability papers (SSE/AIS conferences)
- **S1**: Special projects (Digital Twin)

---

## Status Legend

Each proposal file contains a status indicator:

- 🟢 **READY** - Can start immediately, no blockers
- 🟡 **NEEDS VALIDATION** - Requires technical validation before proceeding
- 🔴 **FUTURE** - Long-term idea, not ready for immediate work
- ⚪ **ON HOLD** - Interesting but lower priority

---

## Quick Reference

| ID | File | Status | Priority | Target |
|----|------|--------|----------|--------|
| E1 | `paper_e1_iac_progressive_learning_learner_lab.md` | 🟡 | ⭐⭐⭐⭐⭐ | MIPRO 2027 |
| E2 | `paper_e2_mcp_infrastructure_assessment_teacher.md` | 🟡 | ⭐⭐⭐ | MIPRO 2027 |
| E3 | `paper_e3_d2_s1_phase4_proposals.md` | 🟢 | ⭐⭐⭐ | MIPRO 2027 |
| D1 | `paper_d1_mcp_observability_incident_response.md` | 🟢 | ⭐⭐⭐⭐⭐ | MIPRO 2027 |
| D2 | `paper_e3_d2_s1_phase4_proposals.md` | 🟢 | ⭐⭐⭐⭐ | MIPRO 2027 |
| D3 | `paper_d3_d4_devops_logging_ideas.md` | 🟢 | ⭐⭐⭐ | MIPRO 2027 |
| D4 | `paper_d3_d4_devops_logging_ideas.md` | 🟢 | ⭐⭐ | MIPRO 2027 |
| S1 | `paper_e3_d2_s1_phase4_proposals.md` | 🔴 | ⭐ | MIPRO 2028+ |

---

## How to Use This Directory

### For Starting a New Paper:

1. **Review Master Index** - Read `MASTER_PAPER_INDEX.md` for complete overview
2. **Choose Proposal** - Select based on priority and validation status
3. **Read Proposal File** - Full details in individual `paper_*.md` files
4. **Complete Validations** - Check "Critical Validation Needed" sections
5. **Execute Plan** - Follow timeline and next steps in proposal

### For Adding a New Idea:

1. Create new file: `paper_<next_id>_<descriptive_name>.md`
2. Use existing proposals as template
3. Update `MASTER_PAPER_INDEX.md` to include new proposal
4. Add to appropriate brainstorming file if needed

### For Tracking Progress:

- Each proposal file has **Next Steps** section
- Mark completed validations with ✅
- Update status (🟡 → 🟢) when validations pass
- Move from proposals to active work when starting

---

## Related Directories

- **`/research/brainstorming/`** - Early-stage ideas, multiple concepts per file
- **`/research/analysis/`** - Paper analysis, literature review, trends
- **`/background/`** - Professional background and expertise
- **`/conference-info/`** - MIPRO conference tracks and details

---

## Critical Next Steps (October 2025)

### Validation Phase - URGENT

**E1 Validation** (This Week):
```bash
[ ] Test Terraform in AWS Academy Learner Lab CloudShell
[ ] Test CloudFormation stack creation
[ ] Check state file storage options
[ ] Make GO/NO-GO decision
```

**E2 Validation** (This Week):
```bash
[ ] Check AWS Academy educator access to student accounts
[ ] Email AWS Academy support about programmatic access
[ ] Test if API credentials available for students
[ ] Make GO/NO-GO decision
```

**D1 Prototype** (Next 2 Weeks):
```bash
[ ] Build basic MCP server for Prometheus
[ ] Build basic MCP server for ADX/Elasticsearch
[ ] Test with historical incident data
[ ] Document results
```

### Decision Point (End of October 2025)

Based on validation results, choose PRIMARY paper:
- **IF E1 viable**: Focus on E1 (IaC Progressive Learning)
- **IF E1 not viable**: Focus on D1 (MCP Observability)
- **IF E2 viable**: Pursue as secondary project

---

## Timeline Overview

**October 2025**: Validation phase
**Nov-Dec 2025**: Development/prototyping
**Jan-Jun 2026**: Pilot studies/data collection
**Jul-Sep 2026**: Analysis and writing
**Oct-Dec 2026**: Refinement
**January 2027**: Submit to MIPRO 2027

---

## Contact

**Researcher**: Marin Kepec
**Institution**: [Your University]
**Role**: DevOps Engineer (Infobip) + AWS Academy Educator
**Target Conference**: MIPRO 2027 (CE or SSE track)

---

## Notes

- All proposals are designed for 6-page MIPRO format
- Each proposal includes methodology, expected contributions, and conference fit
- Technical validation is CRITICAL before committing to E1 or E2
- D1 has no blockers and can start immediately if needed
- Proposals can be combined (e.g., D1 + D2 merged into one comprehensive paper)

---

**For detailed information on any proposal, see the individual `paper_*.md` files.**

**For complete overview and recommendations, see `MASTER_PAPER_INDEX.md`.**

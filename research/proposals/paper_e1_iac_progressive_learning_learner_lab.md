# Paper Proposal: IaC Progressive Learning in AWS Academy Learner Lab

**Status**: Proposed - Needs Technical Validation
**Created**: 2025-12-07
**Target Conference**: CE (Computers in Education) or EE (Engineering Education)
**Priority**: HIGH - Directly leverages your teaching experience

---

## Working Title

"Infrastructure-as-Code for Progressive Cloud Learning: Ensuring Prerequisites and Enabling Skill-Based Assessment in AWS Academy"

---

## Core Concept

Use Infrastructure-as-Code (Terraform or CloudFormation) to solve two critical problems in cloud computing education within AWS Academy Learner Lab:

1. **Weekly Progressive Prerequisites**: Automatically provision consistent starting environments for each lab session
2. **Skill-Based Assessment**: Deploy intentionally broken infrastructure for students to troubleshoot

---

## Problem Statement

Cloud computing courses using AWS Academy Learner Lab face challenges:

### Week-to-Week Dependencies
- **Week 5 problem**: EC2 lab assumes Week 4 VPC was configured correctly
- **Reality**: 30% of students have misconfigured VPCs from previous week
- **Teacher burden**: Hours spent debugging previous week's mistakes instead of teaching new concepts

### Inconsistent Starting Points
- Each student has different infrastructure state
- Makes classroom teaching difficult (everyone seeing different errors)
- Students 3 weeks behind have accumulated configuration debt

### Assessment Limitations
- Traditional exams test memorization, not practical skills
- Cannot measure troubleshooting ability
- No way to assess "can they fix broken infrastructure?"

### Learner Lab Constraints
- $50 budget per student per semester
- 4-hour session windows
- Resources persist between sessions
- Manual cleanup is error-prone

---

## Proposed Solution

### Part A: Weekly IaC Prerequisites

**Before each lab session:**
1. Teacher creates Terraform/CloudFormation module for that week's prerequisites
2. Students run `terraform apply` (or CloudFormation stack) at start of lab
3. Everyone starts from identical, correct infrastructure state
4. Teacher focuses on teaching NEW concepts, not debugging OLD ones

**Example Weekly Progression:**
- **Week 1**: VPC basics → Students learn networking fundamentals
- **Week 2**: EC2 instances → IaC provisions "perfect" VPC, students add EC2
- **Week 3**: Load Balancers → IaC provisions VPC + EC2, students add ALB
- **Week 4**: Databases → IaC provisions web tier, students add RDS
- **Week 5**: Serverless → Complete infrastructure provisioned, students learn Lambda

### Part B: Skill-Based Troubleshooting Assessment

**End-of-semester practical exam:**
1. Teacher creates IaC with intentional errors
2. Students deploy in their Learner Lab
3. Infrastructure fails in specific, educational ways
4. Students must troubleshoot and fix using AWS Console/CLI

**Example Assessment Scenarios:**
- **Security Group Error**: EC2 deployed but SSH port 22 not open
- **Subnet Routing**: Private subnet can't reach internet (missing NAT gateway)
- **IAM Permissions**: Lambda can't access S3 (missing policy)
- **Resource Dependencies**: RDS in wrong VPC or wrong security group
- **Cost Optimization**: t3.2xlarge instead of t3.micro (budget awareness)

---

## 🚨 CRITICAL TECHNICAL VALIDATION NEEDED

### Issue 1: AWS Academy Learner Lab Credentials

**From @temp/AWS Academy Learner Lab.md observations:**

```
Access AWS programmatically:
- AWS CloudShell has credentials pre-configured
- Can run AWS CLI commands
- Can use AWS SDK for Python (boto3)
```

**Key Questions to Investigate:**

1. **Can students run Terraform from CloudShell?**
   - CloudShell is browser-based terminal
   - Terraform requires installation (is it already there?)
   - Can students install Terraform in CloudShell?

2. **Do Learner Lab credentials work with Terraform?**
   - Credentials are temporary (session-based, 4-hour windows)
   - Terraform needs persistent state file
   - Where would state file be stored? (S3 bucket? Local CloudShell?)

3. **Can students run Terraform locally?**
   - Need to export AWS credentials from Learner Lab
   - Are these long-lived enough for local development?
   - Security implications of exporting credentials?

4. **CloudFormation alternative?**
   - CloudFormation is AWS-native (might work better with Learner Lab)
   - Can students create/update/delete stacks via Console or CLI?
   - Does Learner Lab IAM role have CloudFormation permissions?

**Next Steps for Validation:**
```
[ ] Test 1: SSH into CloudShell in Learner Lab
    - Check if Terraform is installed
    - Try to install Terraform if not present
    - Test `terraform --version`

[ ] Test 2: Create simple CloudFormation template
    - Define a t3.micro EC2 instance
    - Try to create stack via AWS Console
    - Try to create stack via AWS CLI in CloudShell
    - Check IAM permissions

[ ] Test 3: Terraform State Management
    - Where to store terraform.tfstate?
    - S3 backend? (does student have S3 bucket?)
    - Local in CloudShell? (does it persist across sessions?)

[ ] Test 4: Session Timeout Handling
    - What happens to Terraform/CloudFormation if session times out?
    - Can students resume after 4-hour limit?
    - Does `terraform apply` need to complete in one session?

[ ] Test 5: IAM Permissions Audit
    - What can LabRole do?
    - Can it create CloudFormation stacks?
    - Can it assume roles needed by Terraform?
    - Any service restrictions?
```

### Issue 2: Student Workflow Feasibility

**Potential Blockers:**
- Students may not know Git (for distributing IaC modules)
- CloudShell file upload/download limitations
- Terraform learning curve on top of AWS concepts
- Debugging IaC errors adds complexity

**Alternative Approaches if IaC Not Viable:**
1. **Manual Scripts**: Bash/Python scripts that call AWS CLI
2. **AWS CDK**: Higher-level abstraction, but adds language dependency
3. **Pre-built AMIs**: Teacher creates AMIs with pre-configured state
4. **Step-by-Step Guides**: Detailed CloudFormation templates students click through

---

## Research Questions

**Primary RQ**: Does the use of Infrastructure-as-Code for progressive lab prerequisites improve student learning outcomes and reduce teacher troubleshooting time compared to traditional "build from scratch each week" approaches?

**Secondary RQ1**: Can skill-based assessments using intentionally broken IaC deployments more accurately measure students' practical cloud troubleshooting abilities than traditional exams?

**Secondary RQ2**: What types of infrastructure errors in IaC-based assessments best distinguish between novice, intermediate, and advanced cloud computing students?

**IF IaC not viable in Learner Lab:**

**Alternative RQ**: Does progressive lab design with pre-configured starting points (via any mechanism) improve learning outcomes compared to cumulative lab approaches?

---

## Methodology

### Phase 1: Technical Feasibility (2-4 weeks)
- Validate Terraform/CloudFormation in Learner Lab
- Test credential mechanisms
- Prototype 2-3 week modules
- Document limitations and workarounds

### Phase 2: Pilot Study (1 semester)
**Study Design**: Single-group pre/post comparison OR two parallel sections

**Pilot Scope**:
- 30-40 students in AWS Academy Cloud Foundations course
- Implement 4-6 weekly IaC modules (not full 12 weeks)
- Create 2-3 troubleshooting assessment scenarios

**Data Collection**:
1. **Learning Outcomes**:
   - Weekly quiz scores
   - Final practical assessment scores
   - AWS service usage logs (CloudTrail data)

2. **Teacher Time**:
   - Hours spent troubleshooting vs teaching (tracked per lab)
   - Number of "my lab doesn't work" help requests
   - Time to grade practical assessments

3. **Student Experience**:
   - Pre/post survey: confidence in cloud skills
   - Survey: lab frustration level
   - Survey: perceived fairness of assessment
   - Open-ended feedback on IaC approach

4. **Budget Metrics**:
   - Do students stay under $50 budget with IaC?
   - Cost comparison: IaC vs manual provisioning

### Phase 3: Analysis & Write-up (2-3 months)
- Statistical analysis of learning outcomes
- Qualitative analysis of student feedback
- Cost-benefit analysis (teacher time saved)
- Paper writing

---

## Expected Contributions

### If IaC Approach is Viable:

**Theoretical**:
- Framework for progressive learning in cloud computing
- Validation of IaC pedagogy
- Taxonomy of infrastructure errors for assessment

**Practical**:
- Open-source repository of weekly Terraform/CloudFormation modules
- Collection of assessment scenarios with rubrics
- Implementation guide for AWS Academy educators

**Pedagogical**:
- Novel assessment method (troubleshooting vs memorization)
- Addresses "theory-practice gap"
- Reproducible, fair, scalable assessment

### If IaC Not Viable, Pivot to:

**Alternative Contribution**:
- Analysis of AWS Academy Learner Lab limitations for education
- Recommendations for AWS Academy product team
- Alternative progressive lab design patterns
- Still valuable for CE/EE conference

---

## Conference Alignment

**CE (Computers in Education)**: Primary target
- Novel teaching methodology
- Addresses real classroom problems
- Tool-enhanced learning

**EE (Engineering Education)**: Secondary target
- Practical skills development
- Industry-relevant tools
- Bridges academia-industry gap

---

## Risk Assessment

### HIGH RISK: IaC May Not Work in Learner Lab

**If Terraform/CloudFormation doesn't work:**
- Paper pivots to "Progressive Lab Design" (without IaC specifics)
- Focus on the pedagogical framework, not the tool
- Still publishable, but less novel

**Mitigation**:
- Early technical validation (do this FIRST)
- Have backup plan (manual provisioning scripts)
- Document WHY it doesn't work (also valuable!)

### MEDIUM RISK: Student Resistance

**If students find IaC too complex:**
- Phase it in gradually (Weeks 1-4 manual, Weeks 5-8 IaC)
- Provide extensive tutorials
- Measure learning curve explicitly

### LOW RISK: IRB Approval

**Educational research requires ethics approval:**
- Start IRB process early
- Likely "exempt" category (normal teaching practice)
- Need opt-in consent for data collection

---

## Timeline

### Q4 2025 (Oct-Dec) - VALIDATION PHASE
- **Critical**: Test IaC in Learner Lab
- Create 2-3 prototype modules
- Get IRB approval
- Plan curriculum integration

### Q1 2026 (Jan-Mar) - PILOT
- Teach AWS Academy course with IaC approach
- Collect data throughout semester
- Conduct troubleshooting assessments

### Q2 2026 (Apr-Jun) - ANALYSIS
- Analyze pilot data
- Student interviews
- Statistical analysis
- Paper writing

### Q3 2026 (Jul-Sep) - SUBMISSION
- Target: MIPRO 2027 (January 2027 deadline)
- Allows time for thorough evaluation
- More realistic than MIPRO 2026

**Alternative Fast Track to MIPRO 2026**:
- If validation happens by October 2025
- Teach Fall 2025 semester with IaC
- Analyze November-December 2025
- Write and submit January 2026
- **VERY TIGHT TIMELINE**

---

## Implementation Details (If Feasible)

### Student Workflow Example

**Week 5 Lab: Adding Load Balancer**

```bash
# 1. Student opens CloudShell in Learner Lab

# 2. Download this week's IaC module
wget https://github.com/prof-marin/aws-labs/week5/main.tf

# 3. Provision prerequisites (VPC + EC2 instances)
terraform init
terraform apply -auto-approve

# Wait ~3 minutes for infrastructure

# 4. Now ready for lab: Add Application Load Balancer
# Instructions: Create ALB in AWS Console that routes to EC2 instances
```

**Benefits**:
- Everyone starts lab with working VPC + EC2
- Lab focuses on NEW concept (ALB), not debugging VPC from Week 4
- Teacher can demo on consistent environment

### Assessment Example

**Practical Exam: "3-Tier Web Application (Broken)"**

```hcl
# main.tf (with intentional errors)
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
  # ERROR 1: Missing security group (students must add)
  # ERROR 2: Wrong subnet (should be public, is private)
}

resource "aws_db_instance" "database" {
  engine         = "mysql"
  instance_class = "db.t3.micro"
  # ERROR 3: In wrong VPC
  # ERROR 4: Publicly accessible = true (security issue)
}

resource "aws_lb" "app_lb" {
  # ERROR 5: Health check path wrong ("/health" doesn't exist)
  # ERROR 6: Not attached to web instances
}
```

**Student Task**:
"Deploy this infrastructure. It should be a working 3-tier web app.
Fix all errors. Document what you fixed and why."

**Grading Rubric** (50 points):
- [ ] EC2 security group allows HTTP (10 pts)
- [ ] EC2 in public subnet (10 pts)
- [ ] RDS in correct VPC (10 pts)
- [ ] RDS not publicly accessible (5 pts)
- [ ] ALB health check fixed (10 pts)
- [ ] ALB routes traffic to EC2 (5 pts)

**Time Limit**: 2 hours

---

## Related Work to Review

**Topics**:
- Infrastructure as Code in education
- AWS Academy teaching methodologies
- Skill-based assessment in CS
- Auto-grading for practical assignments
- Progressive learning frameworks
- "Chaos engineering" in education

**Conferences to Search**:
- Previous MIPRO CE/EE papers
- SIGCSE (CS education)
- ITiCSE (computing education)
- IEEE FIE (engineering education)

---

## Next Steps - IMMEDIATE ACTION REQUIRED

### Step 1: Technical Validation (THIS WEEK)
```
Priority: CRITICAL
Owner: Marin

1. Log into AWS Academy Learner Lab as student
2. Open CloudShell
3. Test Terraform availability/installation
4. Test CloudFormation stack creation
5. Document findings in this file
6. Make GO/NO-GO decision on IaC approach
```

### Step 2: Decision Point (End of Week)
```
IF IaC works:
  → Proceed with this paper idea
  → Start developing weekly modules
  → Plan curriculum integration

IF IaC doesn't work:
  → Pivot to alternative approaches
  → Consider pre-built AMIs
  → OR focus on pedagogical framework without IaC
  → OR pursue different paper idea (MCP assessment)
```

### Step 3: IRB Application (If GO)
```
Start IRB process:
- Describe study design
- Student consent forms
- Data collection plans
- Risk assessment
```

### Step 4: Prototype Development (If GO)
```
Create 3 sample weeks:
- Week 1: VPC module
- Week 3: VPC + EC2 module
- Week 5: Full web tier module

Test with colleague or TA before students
```

---

## Alternative Title Options

1. "Progressive Cloud Infrastructure Learning Using Infrastructure-as-Code in AWS Academy Learner Lab"
2. "From Chaos to Consistency: IaC-Based Lab Prerequisites for Cloud Computing Education"
3. "Automated Lab Environment Management: A Case Study in AWS Academy Cloud Foundations"
4. "Skill-Based Cloud Assessment: Using Intentionally Broken Infrastructure to Measure Troubleshooting Ability"

---

## Notes for Paper Writing

### Introduction Structure
1. **Hook**: "After teaching cloud computing for 5 years, I spend 40% of lab time debugging students' previous week's mistakes..."
2. **Problem**: Week-to-week dependencies, inconsistent environments
3. **Solution**: IaC for progressive prerequisites
4. **Contribution**: Framework + empirical validation + open-source modules

### Key Argument
"Infrastructure-as-Code is not just a DevOps practice—it's a powerful pedagogical tool that ensures consistent learning environments and enables authentic skill assessment."

### Figures Needed
- Figure 1: Traditional vs IaC-based lab progression diagram
- Figure 2: Student learning outcomes comparison (box plots)
- Figure 3: Teacher time breakdown (before/after)
- Figure 4: Example assessment rubric (table)
- Figure 5: Architecture diagram of IaC workflow

### Tables Needed
- Table 1: Weekly module progression
- Table 2: Assessment scenario taxonomy
- Table 3: Student survey results
- Table 4: Cost analysis (budget usage)

---

## Contact for Collaboration

**Potential Co-Authors**:
- Other AWS Academy Educators (multi-institution validation)
- AWS Academy team (product insights)
- CS Education researcher (methodology guidance)

**Open Questions for AWS Academy**:
- Has anyone tried this before?
- Are there AWS Academy guidelines we should follow?
- Would AWS be interested in official support?

---

## Conclusion

**This paper has HIGH potential IF technical validation succeeds.**

The idea is:
- ✅ Novel (no one has done this in AWS Academy)
- ✅ Practical (solves real teaching problem)
- ✅ Feasible (IF IaC works in Learner Lab)
- ✅ Publishable (CE or EE conference)
- ✅ Open-source (benefits community)

**Next action: VALIDATE TERRAFORM/CLOUDFORMATION IN LEARNER LAB**

Without this validation, we're building on uncertain foundation.

**Decision needed by**: End of December 2025 (for MIPRO 2027 timeline)

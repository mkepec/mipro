# Paper Proposal: MCP for AWS Infrastructure Assessment (Teacher Tool)

**Status**: Proposed - Needs Technical Validation & Scope Definition
**Created**: 2025-12-07
**Target Conference**: CE (Computers in Education)
**Priority**: MEDIUM-HIGH - Novel AI application, but complex implementation
**Inspiration**: Paper 08 (LLM Student Assessment for Database Courses)

---

## Working Title

"LLM-Assisted Infrastructure Assessment: Using Model Context Protocol to Evaluate Student AWS Deployments"

---

## Core Concept

Create an MCP server that allows teachers to use LLMs (like Claude) to automatically assess student AWS infrastructure deployments in Learner Lab, similar to how guided labs use grading scripts but for unguided/open-ended assignments.

**Key Parallel to Paper 08**:

| Paper 08 (Database Courses) | This Paper (AWS Infrastructure) |
|-----------------------------|----------------------------------|
| LLM grades SQL queries | LLM verifies AWS resources |
| Checks: query syntax, results | Checks: VPC config, EC2 state, security groups |
| Teacher manually checks DB | Teacher manually checks AWS Console |
| **New**: AI automates grading | **New**: MCP + AI automates checking |

---

## Problem Statement

### Current Manual Assessment Process

**Teacher workflow for checking student AWS work:**
1. Log into AWS Academy educator dashboard
2. Access individual student's Learner Lab workarea
3. Open their AWS Console
4. Manually check: "Did they create VPC correctly?"
5. Verify: "Are there 2 public subnets in different AZs?"
6. Check: "Is EC2 instance in the right subnet?"
7. Verify: "Is security group configured properly?"
8. Check: "Is RDS in private subnet?"
9. Repeat for 40 students × 12 weekly labs = **480 manual checks per semester**

**Time Investment**:
- Simple assignment (VPC + EC2): ~10 minutes per student
- Complex assignment (3-tier app): ~20-30 minutes per student
- **Total per week**: 6-12 hours of grading time

### Why This Problem Exists

**AWS Academy has two types of labs:**

1. **Guided Labs** (e.g., Cloud Foundations):
   - Step-by-step instructions
   - Pre-built grading scripts
   - Automatic verification
   - ✅ Easy to grade (automated)

2. **Learner Lab** (unguided/project-based):
   - Open-ended assignments
   - No built-in grading
   - Manual verification only
   - ❌ Time-consuming to grade (manual)

**This paper focuses on Problem #2**: How to assess student work in Learner Lab when there's no grading script.

---

## Proposed Solution: MCP + LLM Assessment

### Architecture Overview

```
┌─────────────────────────────────────────────┐
│         Teacher (Uses Claude Desktop)       │
│  "Check if student John completed VPC lab" │
└─────────────────┬───────────────────────────┘
                  │ Natural Language
                  ▼
┌─────────────────────────────────────────────┐
│           MCP Server (Python/Node)          │
│  Connects to AWS with student credentials   │
└────────────┬────────────────────────────────┘
             │ AWS SDK (boto3)
             ▼
┌─────────────────────────────────────────────┐
│        Student's AWS Learner Lab            │
│  VPC, EC2, RDS, S3, Security Groups, etc.   │
└─────────────────────────────────────────────┘
```

### MCP Tools for Infrastructure Assessment

```python
# Example MCP Server Tools

@tool
def check_vpc_configuration(student_id: str, assignment_criteria: dict) -> dict:
    """
    Verifies student's VPC matches assignment requirements

    Example criteria:
    {
        "vpc_name": "MyVPC",
        "cidr_block": "10.0.0.0/16",
        "public_subnets": 2,
        "private_subnets": 2,
        "availability_zones": 2
    }
    """
    # Connect to student's AWS account
    # Query VPC configuration
    # Compare to requirements
    # Return assessment

@tool
def check_ec2_instances(student_id: str, requirements: dict) -> dict:
    """
    Verifies EC2 instances meet requirements

    Example requirements:
    {
        "count": 2,
        "instance_type": "t3.micro",
        "in_subnet_type": "public",
        "has_elastic_ip": true,
        "security_group_allows": ["ssh", "http"]
    }
    """

@tool
def check_security_groups(student_id: str, requirements: dict) -> dict:
    """
    Verifies security group rules

    Example:
    {
        "web_sg": {
            "inbound": ["HTTP:80 from 0.0.0.0/0", "SSH:22 from campus"],
            "outbound": ["all"]
        }
    }
    """

@tool
def check_rds_deployment(student_id: str, requirements: dict) -> dict:
    """
    Verifies RDS instance configuration

    Example:
    {
        "engine": "mysql",
        "in_subnet_type": "private",
        "multi_az": false,
        "publicly_accessible": false,
        "backup_enabled": true
    }
    """

@tool
def check_s3_configuration(student_id: str, requirements: dict) -> dict:
    """
    Verifies S3 bucket settings

    Example:
    {
        "bucket_name_pattern": "student-*-website",
        "versioning": true,
        "encryption": true,
        "public_access": false
    }
    """

@tool
def generate_assessment_report(student_id: str, assignment_id: str) -> str:
    """
    Generates comprehensive assessment report for student

    Returns:
    - Checklist of requirements met/missed
    - Grade calculation
    - Specific feedback
    - Suggestions for improvement
    """
```

### Teacher Workflow with MCP

**Scenario: Grading "Week 5 - 3-Tier Web Application"**

**Traditional Approach** (20 minutes per student):
```
1. Open AWS Academy dashboard
2. Click on student name → Workarea → AWS Console
3. Navigate to VPC console → verify subnets
4. Navigate to EC2 console → verify instances
5. Check security groups → verify rules
6. Navigate to RDS console → verify database
7. Check ALB console → verify load balancer
8. Take screenshots for documentation
9. Fill out rubric manually
10. Write feedback comments
```

**MCP-Enhanced Approach** (2-3 minutes per student):
```
Teacher opens Claude Code (or Claude Desktop with MCP)

Teacher: "Grade John's Week 5 assignment"

Claude (via MCP):
1. Reads assignment requirements from rubric
2. Calls check_vpc_configuration(student_id="john")
3. Calls check_ec2_instances(student_id="john")
4. Calls check_security_groups(student_id="john")
5. Calls check_rds_deployment(student_id="john")
6. Calls check_load_balancer(student_id="john")
7. Generates assessment report

Claude outputs:
"Assessment for John Doe - Week 5 Assignment:

✅ VPC Configuration (20/20 points)
   - VPC created with CIDR 10.0.0.0/16
   - 2 public subnets in us-east-1a and us-east-1b
   - 2 private subnets in us-east-1a and us-east-1b
   - Internet Gateway attached
   - Route tables configured correctly

✅ EC2 Instances (15/15 points)
   - 2 t3.micro instances in public subnets
   - Both instances have Elastic IPs
   - Instances running and accessible

⚠️  Security Groups (12/15 points)
   - Web SG allows HTTP (80) ✓
   - Web SG allows SSH (22) ✓
   - ISSUE: SSH allowed from 0.0.0.0/0 (should be campus IP only) ✗
   - Recommendation: Restrict SSH to 10.5.0.0/16

✅ RDS Database (20/20 points)
   - MySQL 8.0 instance created
   - Deployed in private subnets
   - Not publicly accessible ✓
   - Backup retention: 7 days ✓

❌ Load Balancer (0/15 points)
   - No Application Load Balancer found
   - Requirement: ALB should distribute traffic to both EC2 instances
   - Missing component

✅ Cost Optimization (5/5 points)
   - Appropriate instance sizes used
   - Current spend: $3.45 / $50 budget

TOTAL: 72/90 points (80%)

Feedback for Student:
- Great work on VPC and RDS configuration!
- Security concern: Your SSH access is open to the internet.
  Best practice: Restrict to known IP ranges.
- Missing: You haven't created the Application Load Balancer yet.
  See Week 5 instructions section 4.
- Next steps: Create ALB, add target group, configure health checks.

Would you like me to:
1. Email this report to John?
2. Log it in the gradebook?
3. Generate similar reports for all students?"
```

---

## 🚨 CRITICAL TECHNICAL VALIDATION NEEDED

### Issue 1: Teacher Access to Student AWS Accounts

**From AWS Academy Learner Lab Educator Guide observations:**

```
Teachers CAN access student work:
- "How to view and troubleshoot a student's lab workarea" (page 8)
- Teacher clicks: Student → Workarea → AWS Console
- Opens student's AWS Management Console in browser
```

**Key Questions:**

1. **Can teacher get programmatic credentials for student accounts?**
   - GUI access exists (via browser)
   - Programmatic access (AWS CLI/SDK)? Unknown
   - MCP needs API access, not just browser access

2. **Where would MCP server run?**
   - On teacher's laptop? (needs student credentials)
   - In cloud? (centralized service)
   - In AWS Academy infrastructure? (would need AWS support)

3. **Credential mechanism?**
   - Temporary session tokens?
   - Assume role from teacher account?
   - API provided by AWS Academy?

4. **Security & Privacy**:
   - Can teacher programmatically access ALL student accounts?
   - Is there audit log of teacher access?
   - What about student privacy (FERPA)?

**Next Steps for Validation:**
```
[ ] Test 1: Access student workarea via AWS Academy dashboard
    - Log in as teacher
    - Access student's AWS Console
    - Check if "AWS Details" provides CLI credentials
    - Check if teacher can download access keys

[ ] Test 2: AWS Academy API research
    - Does AWS Academy provide an API?
    - Can teachers programmatically query student accounts?
    - Documentation from AWS Academy team?

[ ] Test 3: IAM Role Investigation
    - What IAM permissions does teacher have in student accounts?
    - Can teacher assume a role to get programmatic access?
    - Are there CloudFormation StackSets that could help?

[ ] Test 4: Contact AWS Academy Support
    - Email AWS Academy team
    - Ask: "Can teachers programmatically access student accounts?"
    - Request: API documentation or workarounds

[ ] Test 5: Security Review
    - Would this violate AWS Academy terms of service?
    - Privacy implications of automated access
    - Need institutional approval?
```

### Issue 2: Scope & Feasibility

**Potential Scope Reductions if Full MCP Not Viable:**

**Option A: Screenshot-Based Assessment**
- Teacher takes screenshots of student AWS Console
- Upload to Claude with image recognition
- LLM analyzes screenshots, provides feedback
- Less elegant, but requires no AWS API access

**Option B: Hybrid Approach**
- Teacher manually exports student infrastructure (CloudFormation export)
- MCP analyzes CloudFormation template
- Partial automation, but better than fully manual

**Option C: Student Self-Assessment**
- Students run MCP tool in THEIR OWN Learner Lab
- Get instant feedback before submission
- Shifts from teacher tool to student tool
- Different paper angle (formative vs summative assessment)

**Option D: Focus on Guided Lab Enhancement**
- Instead of Learner Lab (no grading), enhance Guided Labs
- Add MCP layer to existing grading scripts
- Provide detailed explanations of why student failed
- Narrower scope, but more feasible

---

## Research Questions

### If Full MCP Approach is Viable:

**Primary RQ**: Does LLM-assisted infrastructure assessment using Model Context Protocol reduce teacher grading time while maintaining assessment accuracy compared to manual verification?

**Secondary RQ1**: Can LLM-generated feedback on AWS infrastructure deployments improve student learning outcomes compared to traditional manual feedback?

**Secondary RQ2**: What types of AWS infrastructure requirements are most reliably assessed by LLM+MCP vs requiring human judgment?

### If Pivoted to Student Self-Assessment Tool:

**Alternative Primary RQ**: Does providing students with AI-assisted infrastructure verification (via MCP) before submission improve the quality of their final deployments and reduce common errors?

---

## Methodology

### Phase 1: Technical Feasibility (4-6 weeks)
- Validate teacher access to student AWS accounts
- Build prototype MCP server
- Test with 2-3 sample student accounts
- Document limitations

### Phase 2: Pilot Study (1 semester)

**Study Design**: Randomized comparison OR sequential semesters

**Group A**: Traditional manual grading
**Group B**: MCP-assisted grading

**Participants**:
- 1 teacher (you)
- 30-40 students in AWS Academy Learner Lab
- 4-6 assignments throughout semester

**Data Collection**:

1. **Teacher Efficiency**:
   - Time per student assessment (manual vs MCP)
   - Number of assessments completed per hour
   - Teacher satisfaction survey

2. **Assessment Quality**:
   - Inter-rater reliability (manual vs MCP grades)
   - Accuracy: Do MCP assessments match manual assessments?
   - False positives/negatives (infrastructure MCP says is wrong but is actually correct)

3. **Student Outcomes**:
   - Grade improvement on subsequent assignments
   - Student survey: Was feedback helpful?
   - Student survey: Did they understand what to fix?

4. **System Metrics**:
   - MCP query count per assessment
   - AWS API call patterns
   - Error rates (API timeouts, permission issues)

### Phase 3: Analysis (2-3 months)
- Quantitative: Time savings, accuracy metrics
- Qualitative: Teacher and student interviews
- Cost analysis: LLM API costs vs teacher time

---

## Expected Contributions

### If Full MCP Approach Works:

**Technical**:
- Open-source MCP server for AWS infrastructure assessment
- Architecture for secure teacher-student account access
- Reusable assessment criteria for common AWS deployments

**Pedagogical**:
- Evidence for efficacy of AI-assisted grading in cloud education
- Framework for formative feedback on infrastructure work
- Guidelines for what infrastructure aspects need human assessment

**Practical**:
- Scalable grading solution for AWS Academy Learner Lab
- Consistent, detailed feedback for students
- 70-80% reduction in grading time (hypothetical)

### If Pivoted to Student Self-Assessment:

**Different Contributions**:
- Student-facing tool for pre-submission checking
- Formative assessment support
- Reduces teacher burden by improving submission quality
- May be MORE feasible than teacher tool

---

## Conference Alignment

**CE (Computers in Education)**: Primary target
- Novel AI application in education
- Addresses scalability challenges
- Evidence-based pedagogical innovation

**Paper 08 (LLM Student Assessment)** directly inspires this:
- Same conference (CE)
- Same problem domain (automated assessment)
- Different subject (AWS instead of SQL)
- Different mechanism (MCP instead of direct LLM)

---

## Comparison to Paper 08

**Paper 08**: "Exploring the Role of LLMs in Advancing Student Assessment in Database Courses"

| Aspect | Paper 08 | This Paper |
|--------|----------|-----------|
| **Subject** | SQL queries | AWS infrastructure |
| **Assessment Type** | Text-based (SQL syntax, results) | State-based (resource configuration) |
| **Data Access** | LLM queries database directly | MCP queries AWS API |
| **Verification** | Run query, check output | Check resource exists, has correct config |
| **Complexity** | Moderate (query execution) | High (multiple interdependent resources) |
| **Grading Aspects** | Syntax, correctness, efficiency | Existence, configuration, security, networking |
| **Teacher Workflow** | Manual SQL review → LLM review | Manual AWS Console check → MCP check |

**Key Innovation**:
- Paper 08 uses LLMs for textual code analysis
- This paper uses MCP to assess actual infrastructure state
- MCP is the "bridge" between LLM and live AWS accounts

---

## Related Work to Review

**Topics**:
- Automated assessment in CS education (SIGCSE, ITiCSE)
- LLMs in educational assessment
- Cloud computing education
- AWS Academy research
- Model Context Protocol applications
- Infrastructure testing and verification

**Key Papers to Find**:
- Auto-grading systems for programming (Gradescope, etc.)
- LLM applications in education
- Cloud education challenges
- Intelligent tutoring systems

---

## Timeline

### Realistic Timeline (MIPRO 2027):
**Q4 2025 (Oct-Dec)**: Technical validation & feasibility study
**Q1 2026 (Jan-Mar)**: Prototype MCP server development
**Q2 2026 (Apr-Jun)**: Pilot study (Spring semester)
**Q3 2026 (Jul-Sep)**: Analysis & paper writing
**Q4 2026 (Oct-Dec)**: Refinement
**Jan 2027**: Submit to MIPRO 2027

### Aggressive Timeline (MIPRO 2026):
**Oct 2025**: Technical validation
**Nov 2025**: Rapid prototype
**Dec 2025**: Pilot with small group (10 students)
**Jan 2026**: Write & submit
**RISK**: Very tight, likely insufficient data

---

## Risk Assessment

### CRITICAL RISK: No Programmatic Access to Student Accounts

**If teachers cannot get API credentials for student AWS accounts:**
- Full MCP approach NOT viable
- Must pivot to alternative

**Mitigation**:
- Validate early (October 2025)
- Have backup plans (screenshot-based, self-assessment)
- Contact AWS Academy support

### HIGH RISK: MCP Complexity

**Building 5-10 different AWS verification tools:**
- Each AWS service needs separate tool
- Interdependencies (VPC must exist before EC2 check)
- Error handling for missing resources

**Mitigation**:
- Start with 2-3 core services (VPC, EC2, RDS)
- Incremental development
- Reuse existing AWS SDK libraries

### MEDIUM RISK: Assessment Accuracy

**LLM might misinterpret requirements:**
- "2 subnets" – does it mean exactly 2, or at least 2?
- "Public subnet" – how to verify? (route table? IGW?)
- Security rules – many valid configurations

**Mitigation**:
- Very specific rubrics
- Human-in-the-loop for edge cases
- Measure false positive/negative rates

---

## Alternative Angles if Primary Approach Fails

### Angle 1: Student Self-Assessment Tool
**Title**: "AI-Assisted Pre-Submission Verification for Cloud Infrastructure Assignments"
- Students use MCP in their own account
- Get feedback before final submission
- Formative instead of summative assessment

### Angle 2: Guided Lab Enhancement
**Title**: "Explainable AI Feedback for AWS Guided Lab Grading Scripts"
- Add MCP layer to existing guided labs
- Provide detailed explanations of failures
- Help students understand mistakes

### Angle 3: Instructor Dashboard
**Title**: "Visualizing Student AWS Infrastructure: A Dashboard for Cloud Computing Educators"
- Create visualization tool for teacher
- Shows all students' infrastructure at a glance
- Identifies common issues across cohort

### Angle 4: Comparative Study
**Title**: "Manual vs AI-Assisted Assessment in Cloud Computing Education: A Comparative Analysis"
- Compare assessment methods without building full system
- Interview teachers about pain points
- Survey what they wish existed

---

## Next Steps - IMMEDIATE ACTION REQUIRED

### Step 1: Validate Teacher Access (THIS WEEK)
```
Priority: CRITICAL
Owner: Marin

Tasks:
1. Log into AWS Academy as educator
2. Access a student's workarea
3. Check "AWS Details" for credentials
4. Try to use AWS CLI with those credentials
5. Document findings
6. Make GO/NO-GO decision
```

### Step 2: Contact AWS Academy (Next Week)
```
Priority: HIGH
Owner: Marin

Email to: AWS Academy support

Subject: Programmatic access to student Learner Lab accounts for grading

Body:
"I'm an AWS Academy educator exploring ways to improve assessment
of student work in Learner Lab. I'd like to programmatically verify
student AWS infrastructure (VPC, EC2, etc.) to provide faster feedback.

Questions:
1. Can educators programmatically access student AWS accounts?
2. Is there an API for querying student resources?
3. What authentication mechanism would be used?
4. Are there any terms of service concerns?

Use case: AI-assisted grading tool (academic research)

Thanks,
Marin Kepec
AWS Academy Educator"
```

### Step 3: Decision Point (End of October 2025)
```
IF programmatic access possible:
  → Proceed with MCP paper
  → Start prototyping
  → Plan pilot study

IF programmatic access NOT possible:
  → Pivot to student self-assessment angle
  → OR pivot to screenshot-based assessment
  → OR pursue different paper idea (IaC progressive learning)
```

---

## Open Questions

1. **Legal/Privacy**: Does automated access to student accounts violate FERPA?
2. **AWS Academy ToS**: Are educators allowed to build tools like this?
3. **Institutional**: Does university need to approve research protocol?
4. **Student Consent**: Do students need to opt-in to automated assessment?
5. **Data Retention**: Can we store snapshots of student infrastructure?

---

## Conclusion

**This paper has HIGH NOVELTY but UNKNOWN FEASIBILITY.**

Strengths:
- ✅ Directly inspired by Paper 08 (proven concept for CE)
- ✅ Addresses real pain point (teacher grading time)
- ✅ Novel application of MCP (first in cloud education)
- ✅ Aligns with AI/LLM trends

Weaknesses:
- ❌ Technical feasibility UNKNOWN (access to student accounts?)
- ❌ Complex implementation (multiple AWS services)
- ❌ May require AWS Academy support (external dependency)
- ❌ Privacy/security concerns

**Recommendation**:
1. Validate technical feasibility FIRST (October 2025)
2. IF viable → proceed with MCP approach
3. IF not viable → pivot to student self-assessment OR pursue IaC paper instead

**Decision needed by**: End of October 2025

**Most likely outcome**: Pivot to student-facing tool (they run MCP in their own account) rather than teacher-facing tool.

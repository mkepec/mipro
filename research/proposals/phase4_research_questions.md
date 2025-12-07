# Phase 4: Refined Research Questions and Proposals

This document presents the final output of the brainstorming process: a set of specific, actionable research proposals. These ideas are situated at the intersection of your unique expertise and the observed trends at MIPRO, giving them a high potential for acceptance and impact.

---

### Proposal 1: The Cloud-Native Classroom

*   **Refined Research Question:** To what extent does a teaching framework that uses Infrastructure-as-Code (IaC) to manage containerized, cloud-native lab environments improve student learning outcomes and engagement in advanced DevOps topics compared to traditional, manually-configured virtual machine labs?

*   **Problem Statement:** Higher education often struggles to provide students with hands-on lab environments that reflect modern industry practice. Traditional labs are static, hard to scale, and do not effectively teach the principles of cloud-native architecture or automation.

*   **Proposed Methodology:**
    1.  **Develop a Framework:** Design and build an open-source framework using Terraform and Kubernetes to define and deploy "Lab-as-Code." This framework would manage the lifecycle of containerized lab environments for topics like CI/CD, observability, and container security.
    2.  **Comparative Study:** Conduct a study across two student groups in a cloud computing course. One group uses the new framework; the control group uses traditional virtual labs.
    3.  **Data Collection:** Measure learning outcomes via practical assessments and exam scores. Measure engagement and perceived value through surveys and by analyzing system usage logs (e.g., number of lab deployments, time spent).
    4.  **Analysis:** Statistically analyze the quantitative and qualitative data to evaluate the framework's effectiveness.

*   **Expected Contribution:** This paper would contribute a novel, open-source framework for modernizing technology education. It provides empirical evidence of the pedagogical benefits of teaching infrastructure management through the very tools used in industry, directly addressing a key challenge in **CE** and **EE**. The work is also highly relevant for **SSE** and **DC-CPS**.

---

### Proposal 2: The Self-Healing System

*   **Refined Research Question:** Can a large language model (LLM), fine-tuned on historical log, metric, and trace data from a distributed system, generate actionable root cause analysis hypotheses that are more accurate and are generated faster than traditional, alert-based correlation methods?

*   **Problem Statement:** As distributed systems grow in complexity, the volume of observability data makes manual root cause analysis slow and difficult. AIOps aims to solve this, but many solutions are "black boxes." There is a need for intelligent systems that provide human-understandable analysis.

*   **Proposed Methodology:**
    1.  **Data Curation:** Collect and anonymize a large dataset of observability data (logs, metrics, traces from Prometheus, and custom application data) from a real-world, complex application, including periods of normal operation and known incidents.
    2.  **LLM Fine-Tuning:** Fine-tune a moderately-sized open-source LLM (e.g., a Llama or Mistral variant) on the curated dataset. The goal is to train the model to recognize patterns that precede failures and associate them with specific incident types.
    3.  **Develop an XAI Layer:** Integrate the fine-tuned LLM with an Explainable AI (XAI) framework (like SHAP or LIME) to produce not just a conclusion ("*service X is the cause*") but also the reasoning ("*...because of a spike in latency, an increase in 5xx errors, and this specific log message*").
    4.  **Comparative Evaluation:** Benchmark the system's performance against traditional alert-correlation rules and a non-fine-tuned LLM on a held-out test set of incident data. Measure accuracy, time-to-diagnosis, and the quality of the generated explanations.

*   **Expected Contribution:** This paper would provide a concrete architecture for a next-generation AIOps platform, directly addressing the emerging trends of **LLMs** and **XAI** seen in the **AIS** and **SSE** conferences. It builds perfectly on your background in large-scale observability and would be of high interest to industry practitioners.

---

### Proposal 3: The University Digital Twin

*   **Refined Research Question:** What is the feasibility and educational value of a "Digital Twin" of a university's core IT services (e.g., network, identity management, LMS) as a high-fidelity sandbox for teaching advanced cybersecurity and cloud management concepts?

*   **Problem Statement:** Students in cybersecurity and network engineering programs rarely get to work on realistic, production-scale infrastructure. This "theory-to-practice" gap limits their ability to learn critical skills in a safe yet complex environment.

*   **Proposed Methodology:**
    1.  **Architecture Design:** Design a scalable architecture for a real-time Digital Twin of a university's IT landscape. This would involve using automation (Ansible/Terraform) to model the configuration, streaming observability data (Prometheus/Grafana) to model the state, and simulating user traffic.
    2.  **Prototype Implementation:** Build a partial-scope prototype of the Digital Twin, focusing on the networking layer and a key service like the authentication system.
    3.  **Pedagogical Module Development:** Create a set of learning modules that use the Digital Twin for hands-on labs. Examples include a "Red Team/Blue Team" cybersecurity exercise, a "Cloud Migration" simulation, or a "Disaster Recovery" drill.
    4.  **Case Study:** Run a pilot program with a small group of students and gather qualitative data (interviews, surveys) on the perceived realism, educational value, and engagement of the Digital Twin compared to their experience with traditional labs.

*   **Expected Contribution:** This paper would introduce a paradigm-shifting concept for technology education. It is a novel application of **Digital Twin** technology—a hot topic in **SIDE** and **AIS**—to the field of education, making it a compelling, cross-disciplinary submission for **CE**, **EE**, and **CIS**.

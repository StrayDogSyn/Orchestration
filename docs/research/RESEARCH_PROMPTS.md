# Research Prompts for Orchestrator Course Development

**Purpose**: Gather comprehensive data on curriculum design, technical ecosystem, competitive landscape, and justice-focused employment pathways to build the AI Orchestrator bootcamp.

**Research Tools**: 
- Gemini Pro (Prompts 1-3): Broad pedagogical and technical research
- Perplexity Pro (Prompts 4-5): Current market data and tool ecosystem

---

## How to Use This Document

1. **Choose Your Version**: V1 (broader scope) or V2 (justice-focused, free-tier specific)
2. **Copy prompt** → paste into respective tool (Gemini or Perplexity)
3. **Save response** in `docs/research/[tool]-responses/` with filename format: `0X-[topic]-YYYYMMDD.md`
4. **Validate citations** (especially Perplexity - check all links work)
5. **Synthesize findings** after completing all 5 prompts

---

## VERSION COMPARISON

| Aspect | V1 (Initial) | V2 (Revised) |
|--------|--------------|--------------|
| **Scope** | Broad bootcamp analysis | Justice-impacted focus |
| **Tech Emphasis** | General tools | Free-tier specific |
| **Assessment** | Multiple options | Project-based only |
| **Delivery** | Various formats | Self-paced, video-based |
| **Examples** | Lambda School, App Academy | The Last Mile, Persevere |
| **Cost** | Discussed but not central | Zero-cost mandate |

**Recommendation**: Use V2 prompts for building the course. Use V1 prompts if you want broader industry context for comparison or pitching to funders.

---

# GEMINI PRO - PROMPT 1: Curriculum Architecture

## V2 (Revised - Justice-Focused) ⭐ RECOMMENDED

```
I'm designing a 17-24 week self-paced course called "The AI Orchestrator: Agentic Programming 
for Justice-Impacted Developers" that teaches bootcamp graduates and self-taught developers 
to become AI-augmented full-stack engineers. This is NOT "vibe coding" - it's a rigorous 
curriculum emphasizing programming fundamentals enhanced by intelligent LLM orchestration.

CRITICAL CONTEXT:
- Target: Justice-impacted individuals with bootcamp/self-taught background
- Prerequisites: Solid OOP, Big O notation, algorithms, data structures, programming logic
- Economic constraint: Must use free-tier tools exclusively (Gemini, Claude Sonnet free, GPT-4o-mini)
- Goal: Build personal AI agent platform that evolves WITH the developer over time
- Delivery: Self-paced modules with proof-of-concept mini-projects building to capstone
- Philosophy: "Teaching each other" - student teaches AI their domain, AI teaches optimization

RESEARCH OBJECTIVES:

1. PEDAGOGY FOR JUSTICE-IMPACTED LEARNERS IN TECH
   - Successful programs: The Last Mile, Unlocked Futures, Code.7370, Televerde, etc.
   - Barriers beyond curriculum: internet access, hardware limitations, time constraints
   - Retention strategies for self-paced learning without live support
   - Building confidence in students with non-traditional backgrounds
   - Addressing imposter syndrome when learning cutting-edge tech
   - Second-chance employer partnerships and hiring pipeline development

2. CURRICULUM STRUCTURE FOR SELF-PACED MASTERY
   - Optimal module length for self-paced learning (hours per module)
   - Spacing effect and retrieval practice for long-term retention
   - Checkpointing: how to ensure students don't skip fundamentals
   - Project-based assessment: rubrics that test understanding vs. copy-paste
   - Video lecture length and format (screencasts, talking head, hybrid)
   - Supplemental resources: when to use external content vs. create original

3. FUNDAMENTAL CS CONCEPTS AS FOUNDATION FOR AI ORCHESTRATION
   - Why Big O matters when choosing GPT-4 vs. Claude vs. Gemini (cost/speed tradeoffs)
   - Data structures that map to prompt engineering (trees→chain-of-thought, graphs→multi-agent)
   - Algorithm design patterns that inform LLM workflow orchestration
   - How understanding compilers/interpreters helps debug prompt behavior
   - Vectorization concepts for embeddings and semantic search
   - Random forests/decision trees as mental models for AI decision-making

4. ZERO-COST INFRASTRUCTURE ARCHITECTURE
   - Free-tier LLM API limits and strategies to stay within them
   - GitHub Student Developer Pack: what's included, how to maximize
   - Google Colab vs. Kaggle Notebooks: feature comparison, persistence strategies
   - Free vector DB options: ChromaDB local, Pinecone free tier, Weaviate Cloud
   - Vercel/Netlify/GitHub Pages: deployment limits and cost avoidance
   - MongoDB Atlas free tier, Supabase free tier for persistence

5. "ORGANIC EVOLUTION" LEARNING MODEL
   - How do developers and AI tools co-evolve through repeated interaction?
   - Documented case studies: programmers who improved via AI pair programming
   - Cognitive apprenticeship models applied to human-AI collaboration
   - Metacognition: teaching students to reflect on what AI does well vs. poorly
   - Building mental models: when to trust AI, when to verify, when to override

DELIVERABLES REQUESTED:
- Module structure template: objectives → mini-lecture → hands-on lab → proof-of-concept project
- Assessment rubrics that distinguish "understanding" from "copying"
- Resource curation guidelines: finding quality YouTube/article content
- Retention checkpoints: "If you can't do X without AI, go back to Module Y"
- Analogies and mental models for technical concepts (cooking, gaming, movies, etc.)
- Risk mitigation: common drop-off points and intervention strategies

Please cite research on adult learning, technical education for non-traditional students, 
and human-AI collaboration. Prioritize evidence-based practices that have worked in 
justice-focused tech education programs.
```

## V1 (Initial - Broader Scope)

```
I'm designing a 17-24 week bootcamp-style course on "AI-Augmented Software Development" that teaches 
students to become hybrid developers who leverage LLMs as learning and development tools while 
maintaining strong foundational programming skills. This is not a course on building AI systems, 
but rather using AI tools to enhance human software development capabilities.

TARGET CONTEXT:
- Students have basic Python/JavaScript fundamentals (variables, functions, loops, basic OOP)
- Many students are career changers, including justice-impacted individuals
- Goal is job-ready skills for roles like AI Solutions Engineer, Augmented Developer, or Prompt Engineer
- Course delivery: Cohort-based with synchronous and asynchronous components

RESEARCH OBJECTIVES:

1. CURRICULUM FRAMEWORKS FOR TECHNICAL BOOTCAMPS
   - Analyze successful 12-24 week bootcamp structures (Lambda School, App Academy, etc.)
   - Identify optimal pacing for skill building vs. project work vs. job prep
   - Best practices for cohort-based learning in technical education
   - Spaced repetition and retrieval practice in coding education

2. LEARNING PROGRESSIONS FOR AI LITERACY
   - How do professionals currently learn prompt engineering? (courses, self-study, on-the-job)
   - Cognitive load considerations when teaching AI tool usage alongside programming
   - Scaffolding strategies: when to introduce AI assistance vs. require manual work
   - Assessment methods that test understanding, not just AI-generated outputs

3. INDUSTRY-RELEVANT SKILL TAXONOMIES
   - What competencies define an "AI-augmented developer" vs traditional SWE?
   - Token economics and cost management: what do employers expect entry-level hires to know?
   - Tool orchestration: which workflows are industry-standard vs. experimental?
   - Model selection strategies: how do professionals choose between GPT-4, Claude, Gemini, etc.?

4. PEDAGOGICAL MODELS FOR HYBRID LEARNING
   - Flipped classroom approaches for technical skills
   - Project-based learning scaffolds for complex, multi-week builds
   - Peer learning and code review structures
   - Mentorship models that scale (1:15+ ratios)

5. EQUITY AND ACCESS CONSIDERATIONS
   - Cost barriers: API usage, compute resources, tooling subscriptions
   - Digital divide concerns: internet reliability, hardware requirements
   - Support structures for non-traditional students (career changers, justice-impacted, etc.)
   - Accommodations for different learning speeds and styles

DELIVERABLES REQUESTED:
- Recommended week-by-week pacing template (12-week vs. 24-week comparison)
- Suggested assessment milestones and portfolio project checkpoints
- Resource allocation estimates (instructor time, API costs, cloud credits)
- Learning objective hierarchies (Bloom's taxonomy adapted for AI-augmented development)
- Risk factors and common failure modes in similar programs

Please provide academic research citations, case studies from existing bootcamps, and 
pedagogical frameworks that support your recommendations. Prioritize evidence-based 
practices over theoretical models.
```

---

# GEMINI PRO - PROMPT 2: Technical Deep-Dive

## V2 (Revised - Orchestration Focus) ⭐ RECOMMENDED

```
I'm building a technical curriculum for "AI Orchestrators" - developers who maintain strong 
CS fundamentals while leveraging LLMs as collaborative tools for complex problem-solving. 
This is NOT about replacing programming skills with prompts, but enhancing engineering 
judgment through intelligent tool selection and workflow design.

CORE PRINCIPLE: "Learn the fundamentals so deeply that you know when AI helps vs. when it hinders."

TECHNICAL DOMAINS TO RESEARCH:

1. FOUNDATIONS: WHY FUNDAMENTALS MATTER MORE WITH AI
   - The "Chinese Mail Room" problem: why you can't outsource understanding
   - Big O applied to LLM selection: O(1) for Haiku, O(n) for Sonnet, O(n²) for Opus
   - Data structures as prompt architecture: lists, trees, graphs, hash maps
   - Algorithm patterns in prompt engineering: divide-and-conquer, dynamic programming, greedy
   - Type systems and why Claude 3.5 understands Python typing better than Claude 2
   - Debugging AI outputs requires debugging mental models: stack traces for prompts

2. PROMPT ENGINEERING AS A PROGRAMMING DISCIPLINE
   - Prompt = function signature: inputs, outputs, side effects, error handling
   - System prompts as "class constructors" for AI behavior
   - Few-shot learning = unit tests for prompts
   - Chain-of-thought = explicit algorithm walk-throughs
   - Role-based prompting = interface segregation principle
   - Iteration and refinement cycles: prompt versioning and A/B testing
   - Common anti-patterns: vague instructions, under-specified outputs, no constraints

3. MODEL ORCHESTRATION AND LOAD BALANCING
   - Decision tree: which model for which task? (speed vs. quality vs. cost)
   - Parallel processing: sending requests to multiple models simultaneously
   - Fallback chains: GPT-4o-mini → Claude Sonnet → Gemini Pro → local Llama
   - Rate limiting and backoff strategies to stay in free tiers
   - Context window management: splitting tasks vs. summarizing vs. caching
   - Token counting and budget allocation across a multi-step pipeline
   - Benchmarking: building test suites to compare model performance on your tasks

4. TOOL AND WORKFLOW DESIGN
   - Function calling and tool use: when AI needs to execute code
   - Multi-agent systems: specialized AI "microservices" vs. monolithic prompts
   - State machines for conversation flows (e.g., troubleshooting wizard)
   - Error handling: what to do when LLM hallucinates or refuses
   - Human-in-the-loop patterns: when to require confirmation vs. automate
   - Logging and observability: tracking prompts, outputs, and iterations
   - Version control for prompts: treating prompts as code artifacts

5. MEMORY AND PERSISTENCE ARCHITECTURE
   - Short-term: conversation history within a session
   - Long-term: vector embeddings in ChromaDB or Pinecone
   - Hybrid: SQL for structured data + vector DB for semantic search
   - RAG (Retrieval-Augmented Generation): when to use, how to implement
   - Conversation summarization strategies to extend context windows
   - Privacy and security: keeping sensitive data out of LLM training
   - Graceful degradation: what happens when vector DB is unavailable?

6. BUILDING YOUR PERSONAL AI AGENT PLATFORM
   - Architecture: modular design for extensibility
   - Core modules: prompt library, model router, memory system, tool executor
   - Configuration management: environment variables, secrets, API keys
   - Testing: how to validate non-deterministic systems
   - Deployment: packaging for personal use vs. sharing with others
   - Documentation: explaining your system to future you (or future employers)
   - Evolution: versioning your AI agent as you learn new techniques

DELIVERABLES REQUESTED:
- Sequential learning modules with prerequisite chains clearly marked
- Hands-on labs for each concept (e.g., "Build a model router in 50 lines of Python")
- Mini-projects that combine multiple concepts (e.g., "RAG-powered code reviewer")
- Analogies from cooking, gaming, and 90s movies for each major concept
- Code templates and starter repos for common patterns
- "Before and After" examples: naive implementation → optimized orchestration
- Troubleshooting guides: "If your prompt isn't working, check these 7 things"

Focus on Python as primary language (JavaScript for web deployment). Assume free-tier 
constraints for all tools. Prioritize practical patterns over theoretical frameworks.
```

## V1 (Initial - Broader Technical Survey)

```
I'm developing a comprehensive technical curriculum for teaching AI-augmented software development. 
This course teaches developers to leverage LLMs as collaborative tools while building strong 
foundational skills. I need a detailed technical roadmap covering prompt engineering, model 
selection, tool orchestration, and workflow optimization.

TECHNICAL DOMAINS TO RESEARCH:

1. PROMPT ENGINEERING CURRICULUM
   - Progression from basic prompts → advanced techniques (chain-of-thought, few-shot, role-based)
   - System prompt design and context management
   - Prompt templating and reusability patterns
   - Debugging and iteration strategies for prompts
   - Domain-specific prompting (code generation, debugging, documentation, testing)
   - Anti-patterns and common mistakes

2. TOKEN ECONOMICS AND MODEL SELECTION
   - Understanding context windows, token limits, and pricing models
   - Cost-benefit analysis: when to use GPT-4 vs. Claude Sonnet vs. Gemini Pro vs. local models
   - Batch processing strategies to minimize API costs
   - Caching and conversation management for efficiency
   - Monitoring usage and setting budgets programmatically

3. TOOL AND WORKFLOW ORCHESTRATION
   - Multi-agent systems and tool chaining
   - LangChain, LlamaIndex, and similar frameworks: when to use vs. build custom
   - API integration patterns (REST, WebSockets, streaming responses)
   - Error handling and fallback strategies when LLMs fail
   - Version control for AI-augmented code (tracking human vs. AI contributions)

4. MEMORY SYSTEMS AND CONTEXT MANAGEMENT
   - Short-term vs. long-term memory architectures
   - Vector databases and semantic search (Pinecone, Weaviate, ChromaDB)
   - Retrieval-Augmented Generation (RAG) implementation patterns
   - Conversation state management across sessions
   - Privacy and security considerations for persistent memory

5. CUSTOM MODEL FINE-TUNING AND TRAINING
   - When fine-tuning is worth the investment vs. prompt engineering
   - Dataset creation and annotation for fine-tuning
   - Transfer learning basics for developers (not data scientists)
   - Evaluation metrics for custom models
   - Cost and complexity considerations (cloud vs. local training)

6. REAL-WORLD INTEGRATION PATTERNS
   - Building AI-first applications vs. adding AI to existing apps
   - Testing strategies for non-deterministic systems
   - Production deployment and monitoring
   - Fallback strategies and graceful degradation
   - User feedback loops and iterative improvement

DELIVERABLES REQUESTED:
- Sequenced learning modules with estimated time per topic (hours of instruction + practice)
- Hands-on lab exercises and project ideas for each domain
- Prerequisite knowledge checks and readiness assessments
- Common pitfalls and troubleshooting guides
- Tool and framework comparison matrices
- Code examples and starter templates
- Reading lists (documentation, papers, blog posts)

Please include current state-of-the-art practices as of 2024-2025, noting which techniques 
are emerging vs. established. Prioritize practical, production-ready patterns over 
research prototypes.
```

---

# GEMINI PRO - PROMPT 3: Portfolio Projects

## V2 (Revised - Zero-Cost Projects) ⭐ RECOMMENDED

```
I need a progression of portfolio projects for an "AI Orchestrator" bootcamp where students 
build a personal AI agent platform that evolves with them over 17-24 weeks. Each project 
must demonstrate mastery without being copyable from ChatGPT - they require design thinking, 
debugging, and iterative refinement.

PROJECT DESIGN PRINCIPLES:
- Must work on free-tier APIs (Gemini, Claude Sonnet free, GPT-4o-mini)
- Deployable on GitHub Pages, Vercel free tier, or local environment
- Each project builds skills needed for the final capstone
- Assessment: "Does it work?" + "Can you explain your design choices?"
- No project should take more than 8-12 hours of focused work

PROGRESSIVE PROJECT SEQUENCE:

1. WEEKS 1-3: FUNDAMENTALS + BASIC PROMPTING
   Mini-Project: "Personal Code Explainer"
   - Takes a code snippet as input
   - Uses Gemini/Claude to explain it line-by-line
   - Student must validate explanations (tests understanding of fundamentals)
   - Teaches: prompt structure, API calls, output parsing
   - Success: Can explain why AI's explanation is right or wrong

2. WEEKS 4-6: MODEL SELECTION + LOAD BALANCING
   Mini-Project: "Smart Model Router"
   - Accepts a task description
   - Classifies it as simple/medium/complex
   - Routes to appropriate free-tier model (Haiku → Sonnet → Opus equivalent)
   - Tracks token usage and stays under free limits
   - Teaches: decision trees, cost optimization, rate limiting
   - Success: Handles 50 diverse tasks without exceeding free tier

3. WEEKS 7-9: MEMORY + PERSISTENCE
   Mini-Project: "Learning Flashcard System"
   - Stores Q&A pairs with embeddings (ChromaDB local)
   - Retrieves similar questions when new one asked
   - Uses RAG to generate answers based on past learning
   - Teaches: vector databases, semantic search, RAG patterns
   - Success: "Remembers" material better over time (spaced repetition)

4. WEEKS 10-12: MULTI-AGENT + TOOL USE
   Mini-Project: "Code Review Assistant"
   - Linter agent: checks style/syntax
   - Logic agent: analyzes algorithm efficiency
   - Test agent: suggests test cases
   - Aggregator agent: combines feedback into report
   - Teaches: agent orchestration, tool calling, output aggregation
   - Success: Provides actionable code review on real student code

5. WEEKS 13-17: CAPSTONE - PERSONAL AI AGENT PLATFORM
   Requirements:
   - Modular architecture (easy to add new capabilities)
   - Model orchestration (routes tasks to best available model)
   - Persistent memory (learns from interactions)
   - Tool integration (can run code, search docs, etc.)
   - Conversation management (maintains context)
   - Self-documentation (AI helps explain its own architecture)
   
   Must demonstrate:
   - Clean code with proper error handling
   - Configuration management (API keys, settings)
   - Testing strategy for non-deterministic behavior
   - Deployment instructions (reproducible setup)
   - Video demo explaining design choices
   
   Teaches: Systems thinking, software architecture, DevOps basics
   Success: Platform that actually helps student in their daily coding work

6. WEEKS 18-24 (OPTIONAL): SPECIALIZATION TRACKS
   - Track A: Web deployment (FastAPI + Vercel)
   - Track B: Data analysis agent (pandas + visualization)
   - Track C: Creative applications (story generator, game NPC)
   - Track D: Open-source contribution (improve existing AI tool)

ASSESSMENT RUBRICS NEEDED:
- Technical execution (does it work? is code clean?)
- Design rationale (why these choices? what tradeoffs?)
- Problem-solving (how did you debug? what did you learn?)
- Orchestration skill (using AI tools effectively during build)
- Documentation (can someone else understand your system?)

DELIVERABLES REQUESTED:
- Detailed project briefs with success criteria
- Starter templates with TODOs (not full solutions)
- Example solutions for instructors (not shared with students)
- Common pitfalls and debugging strategies
- Rubrics that test understanding, not just functionality
- "Organic evolution" checkpoints: how should AI agent improve by Week X?

Please suggest video content, articles, and resources that students can use to learn 
concepts before starting each project. Focus on free, high-quality sources.
```

## V1 (Initial - General Portfolio Design)

```
I'm designing portfolio projects for a bootcamp on AI-augmented software development. Students 
need to demonstrate proficiency in prompt engineering, model selection, tool orchestration, 
and real-world problem-solving using LLMs as development partners.

PROJECT DESIGN RESEARCH:

1. PORTFOLIO ARCHITECTURE FOR AI-AUGMENTED DEVELOPERS
   - What do hiring managers look for in portfolios for AI-related roles?
   - How should candidates demonstrate AI literacy vs. traditional coding skills?
   - Documentation standards: explaining AI contributions vs. human design decisions
   - GitHub repo structure and README best practices for AI projects

2. PROGRESSIVE COMPLEXITY PROJECTS
   - Week 3-4: Beginner project ideas (simple prompt-based tools)
   - Week 8-9: Intermediate project ideas (multi-model systems, basic RAG)
   - Week 16-17: Advanced project ideas (custom fine-tuning, production deployment)
   - Capstone project: 3-4 week builds that demonstrate job-ready skills

3. INDUSTRY-ALIGNED PROJECT THEMES
   - Customer support chatbot with knowledge base integration
   - Code review assistant with context-aware suggestions
   - Documentation generator that maintains consistency across codebases
   - Data analysis tool with natural language querying
   - Personal learning assistant with spaced repetition
   - Creative applications (writing tools, game NPCs, music generators)

4. ASSESSMENT RUBRICS
   - Technical execution (code quality, architecture, error handling)
   - AI integration (effective prompting, appropriate model selection, cost efficiency)
   - Problem-solving (requirements analysis, iterative refinement, testing)
   - Documentation (clear explanations, reproducible setup, API key security)
   - Presentation (demo skills, technical communication, storytelling)

5. REAL-WORLD CONSTRAINTS SIMULATION
   - Budget limits ($50 API budget for capstone project)
   - Time constraints (48-hour hackathon-style sprints)
   - Team collaboration (pair programming with AI assistance)
   - Legacy code integration (adding AI to existing codebases)
   - Accessibility and ethical considerations

DELIVERABLES REQUESTED:
- 10-15 project briefs with detailed requirements and success criteria
- Scaffolding templates and starter code for each project
- Assessment rubrics with scoring guides
- Timeline templates (Gantt charts for multi-week projects)
- Common blockers and instructor intervention points
- Example portfolio structures for graduates to emulate

Please include links to exemplary public projects, GitHub repos, and portfolio sites that 
demonstrate best practices in this emerging field.
```

---

# PERPLEXITY PRO - PROMPT 4: Market Analysis

## V2 (Revised - Second-Chance Focus) ⭐ RECOMMENDED

```
I'm researching the market landscape for an "AI Orchestrator" bootcamp targeting justice-impacted 
developers. I need competitive intelligence, salary data, hiring trends, and partnership opportunities 
focused on second-chance employment in tech.

RESEARCH QUESTIONS:

1. SECOND-CHANCE TECH EMPLOYMENT ECOSYSTEM
   - Companies with explicit "second-chance" hiring programs (List 20+ with links)
   - Tech firms partnered with The Last Mile, Televerde, Persevere, Unlocked Futures
   - Remote-first companies open to justice-impacted candidates (List 30+)
   - Background-check policies in tech: which companies have "ban the box"?
   - Success stories: justice-impacted individuals who landed AI/ML roles
   - Salary ranges: do second-chance hires get market-rate pay?

2. AI-AUGMENTED DEVELOPER JOB MARKET (2024-2025)
   - Job titles: "AI Solutions Engineer," "Prompt Engineer," "ML Ops," "AI Orchestrator"
   - Required skills in job postings: coding + AI tools (analyze 50+ recent postings)
   - Salary data: entry-level AI roles vs. traditional junior SWE
   - Geographic distribution: where are these jobs? Remote %?
   - Certifications mentioned: AWS ML, Google Cloud AI, vendor-specific (Anthropic, OpenAI)
   - Portfolio expectations: what do employers want to see?

3. COMPETITIVE LANDSCAPE: AI-FOCUSED BOOTCAMPS
   - Existing programs teaching prompt engineering, AI development, LLM orchestration
   - Price points, duration, job placement rates, student demographics
   - Curriculum highlights: what topics do they cover?
   - Reviews and outcomes: student testimonials, employer feedback
   - Gaps: what skills are employers wanting that programs aren't teaching?

4. FREE-TIER TOOL ECOSYSTEM FOR LEARNERS
   - GitHub Student Developer Pack: full list of included tools + credit amounts
   - Free LLM API limits: Gemini, Claude, GPT (requests/day, tokens, rate limits)
   - Free compute: Google Colab vs. Kaggle Notebooks (GPU access, session limits)
   - Free vector DBs: Pinecone, Weaviate Cloud, Qdrant Cloud (storage limits)
   - Free deployment: Vercel, Netlify, GitHub Pages (bandwidth, build minutes)
   - Total cost analysis: can a student complete 24-week bootcamp for $0?

5. JUSTICE-FOCUSED FUNDING AND PARTNERSHIPS
   - Grants for justice-impacted tech education (Chan Zuckerberg, Vera Institute, etc.)
   - Corporate sponsorships for second-chance programs (Google.org, Microsoft, etc.)
   - Foundations funding criminal justice reform + tech workforce development
   - Government programs: Pell Grants for incarcerated students, reentry services
   - Potential partnerships: YCombinator for Social Good, Fast Forward, etc.

6. CERTIFICATION AND CREDENTIALING OPTIONS
   - Do employers value bootcamp certificates for AI roles?
   - Micro-credentials: Credly badges, digital certificates, blockchain credentials
   - Portfolio-first hiring: companies that skip degrees/certs for demonstrated skill
   - Open-source contributions as credibility signals
   - Creating a new certification: legal requirements, accreditation considerations

DELIVERABLE FORMAT:
- Comparison table: 10+ competing AI bootcamps with price, duration, outcomes
- Job market report: 50+ job posting analysis with skill requirements + salary ranges
- Second-chance employer database: 50+ companies with contact info + hiring programs
- Free tool matrix: limits, features, workarounds for each platform
- Funding opportunities: 20+ grants/partnerships with application deadlines
- Recommended credentialing strategy based on employer priorities

Please prioritize 2024-2025 data with direct links to sources. Flag any information that 
may be outdated or requires verification.
```

## V1 (Initial - General Market Analysis)

```
I'm launching a bootcamp on AI-augmented software development and need competitive intelligence 
on existing programs, market gaps, and pricing strategies.

RESEARCH QUESTIONS:

1. EXISTING PROGRAMS AND COURSES
   - What bootcamps, courses, or programs currently teach prompt engineering or AI-augmented development?
   - Include: price points, duration, curriculum highlights, student outcomes/job placement rates
   - Identify leaders in this space: Bloom Institute, Correlation One, vendors like OpenAI/Anthropic
   - What do reviews and student testimonials highlight as strengths/weaknesses?

2. MARKET GAPS AND OPPORTUNITIES
   - What skills do employers want that current programs don't teach?
   - Job postings analysis: "Prompt Engineer," "AI Solutions Engineer," "ML Ops" - what do they require?
   - Salary ranges for AI-augmented developer roles vs. traditional SWE roles
   - Geographic concentrations: where are these jobs located? Remote-friendly?

3. CERTIFICATION AND CREDENTIALING
   - Do any recognized certifications exist for prompt engineering or AI development?
   - What credentials do employers value? (AWS ML certs, Google Cloud AI, vendor-specific?)
   - Would a custom certificate from this program hold value, or is portfolio more important?

4. PRICING AND BUSINESS MODELS
   - Typical bootcamp costs: upfront vs. ISA (Income Share Agreement) vs. deferred tuition
   - Scholarship and financial aid models for underrepresented groups
   - Corporate training programs: do companies pay for AI upskilling for existing engineers?
   - Free/low-cost alternatives: what's available on Coursera, Udacity, YouTube?

5. INDUSTRY PARTNERSHIPS AND PLACEMENT
   - Which companies actively hire from AI-focused bootcamps?
   - Internship or apprenticeship programs that bridge learning → employment
   - Tech communities and networks for AI developers (Discord, Slack groups, conferences)

DELIVERABLE FORMAT:
- Comparison table of 5-10 competing programs
- Market analysis with citations to job boards, salary sites, industry reports
- SWOT analysis: opportunities for differentiation
- Recommended partnerships or affiliations to explore

Please prioritize recent data (2024-2025) and include direct links to sources.
```

---

# PERPLEXITY PRO - PROMPT 5: Tech Ecosystem

## V2 (Revised - Free-Tier Focus) ⭐ RECOMMENDED

```
I need a comprehensive survey of current tools, platforms, and frameworks that an AI-augmented 
developer should know in 2025. This is for a bootcamp curriculum covering practical, 
production-ready technologies with ZERO-COST constraint (all free tiers).

TOOL CATEGORIES TO RESEARCH:

1. FREE-TIER LLM COMPARISON (2025 STATE-OF-THE-ART)
   - Google Gemini: models, rate limits, unique features, best use cases
   - Anthropic Claude: Sonnet/Opus free access, API limits, strengths/weaknesses
   - OpenAI GPT: 4o-mini vs. 3.5-turbo, free tier details, when to use each
   - Open-source: Llama 3.x, Mixtral, Phi-3 - local vs. cloud hosting options
   - Comparison matrix: speed, quality, context window, multimodal, pricing
   - Community consensus: which model for which tasks? (Reddit, Discord, X threads)

2. ZERO-COST INFRASTRUCTURE PATTERNS
   - Vector databases: ChromaDB (local), Pinecone (free tier limits), Weaviate Cloud
   - Deployment: Vercel vs. Netlify vs. GitHub Pages (bandwidth, build limits, features)
   - Compute: Google Colab vs. Kaggle vs. Lightning AI Studios (GPU access, persistence)
   - Storage: MongoDB Atlas free, Supabase free, Planetscale free, Firestore
   - Monitoring: free observability tools for LLM apps (logs, traces, usage tracking)
   - How to architect systems to stay free: caching, batch processing, queue management

3. DEVELOPMENT TOOLS + IDES FOR AI WORKFLOWS
   - VSCode extensions: Copilot alternatives (Codeium, Tabnine free tiers)
   - Jupyter alternatives: Marimo, Google Colab, Kaggle Notebooks, Observable
   - Prompt engineering tools: PromptLayer free tier, LangSmith free tier, custom solutions
   - Testing frameworks: pytest for LLM apps, evaluation datasets, benchmarking tools
   - Version control: Git + GitHub for prompt versioning, config management
   - CI/CD for AI apps: GitHub Actions free tier, automated testing strategies

4. LEARNING RESOURCES + COMMUNITY HUBS (2025 ACTIVE)
   - YouTube channels: AI engineering tutorials, prompt engineering deep-dives
   - Blogs/newsletters: must-follow sources for LLM development
   - Discord servers: active communities for AI developers (links + member counts)
   - Reddit: r/MachineLearning, r/LocalLLaMA, r/PromptEngineering - quality threads
   - GitHub repos: awesome lists, starter templates, example projects
   - Courses: free MOOCs, vendor tutorials (Anthropic, OpenAI, Google)
   - Conferences/meetups: AI engineering events, virtual options

5. PRODUCTION PATTERNS FOR LLM APPLICATIONS
   - Architecture patterns: monolithic vs. microservices for AI agents
   - Error handling: retries, fallbacks, circuit breakers for LLM calls
   - Security: API key management, rate limiting, input validation
   - Observability: logging prompts + outputs, debugging non-deterministic behavior
   - Testing: unit tests, integration tests, end-to-end tests for AI systems
   - Deployment: Docker, serverless, edge functions - pros/cons for each
   - Real-world case studies: production LLM apps built on free/cheap infrastructure

6. EMERGING TOOLS + TRENDS TO WATCH
   - New frameworks: what's gaining traction in 2024-2025?
   - Model-as-a-service: new platforms offering free tiers
   - Agentic frameworks: AutoGPT, BabyAGI, CrewAI - status and utility
   - Multi-modal capabilities: image, audio, video in free-tier models
   - Fine-tuning platforms: any free options for custom model training?
   - AI coding assistants: evolution beyond Copilot, competitive landscape

DELIVERABLE FORMAT:
- Free-tier comparison table: all tools with limits, features, gotchas
- Recommended tech stack: beginner → intermediate → advanced
- Setup guides: step-by-step for zero-cost dev environment
- Community resource directory: active links with descriptions
- Production deployment checklist: from local dev to public app
- Tool radar: what's new/hot vs. what's declining/deprecated

Please prioritize tools with:
- Active development (commits in last 3 months)
- Good documentation (official docs + community tutorials)
- Strong community (active Discord/Reddit, quick issue responses)
- Clear free tier (no credit card required to start)

Include direct links to docs, repos, Discord invites, and example projects.
```

## V1 (Initial - General Tool Survey)

```
I need a comprehensive survey of current tools, platforms, and frameworks that an AI-augmented 
developer should know in 2025. This is for a bootcamp curriculum covering practical, 
production-ready technologies.

TOOL CATEGORIES TO RESEARCH:

1. LLM PROVIDER PLATFORMS
   - OpenAI API (GPT-4, GPT-4 Turbo, embeddings): pricing, features, best use cases
   - Anthropic Claude (Sonnet, Opus, Haiku): pricing, features, unique capabilities
   - Google Gemini (Pro, Ultra): availability, pricing, integration patterns
   - Open-source models (Llama 3, Mixtral, Phi-3): hosting options, performance benchmarks
   - Comparison matrix: cost, speed, quality, context windows, multimodal support

2. DEVELOPMENT FRAMEWORKS AND LIBRARIES
   - LangChain: when to use, common patterns, limitations, community resources
   - LlamaIndex: RAG-specific features, comparison to LangChain
   - Hugging Face ecosystem: Transformers, Datasets, Spaces
   - Alternative frameworks: Haystack, Semantic Kernel, AutoGen
   - API client libraries and SDKs for major LLM providers

3. VECTOR DATABASES AND SEMANTIC SEARCH
   - Pinecone, Weaviate, Qdrant, ChromaDB: feature comparison, pricing, scalability
   - Which are best for prototyping vs. production?
   - Integration with LLM frameworks (native LangChain/LlamaIndex support)
   - Open-source vs. managed options

4. DEPLOYMENT AND INFRASTRUCTURE
   - Hosting options: Vercel, Netlify, Replit, AWS, Google Cloud, Azure
   - Serverless vs. container-based deployments for LLM apps
   - API management and rate limiting tools (Kong, Tyk, cloud-native options)
   - Monitoring and observability: LangSmith, Helicone, Weights & Biases
   - Cost optimization tools and strategies

5. DEVELOPMENT ENVIRONMENTS AND TOOLING
   - IDEs with AI assistance: Cursor, Codeium, GitHub Copilot
   - Notebook environments: Jupyter, Google Colab, Kaggle
   - Prompt engineering tools: PromptLayer, PromptPerfect, playground UIs
   - Testing frameworks for LLM applications
   - Version control for prompts and model configurations

6. LEARNING RESOURCES AND COMMUNITIES
   - Top documentation sites, tutorials, and guides
   - Active communities: Reddit, Discord servers, Slack workspaces
   - Conferences and meetups focused on AI development
   - Newsletter and blog recommendations
   - YouTube channels and podcast series

DELIVERABLE FORMAT:
- Tool comparison tables with pricing, pros/cons, learning curve
- Recommended tech stack for course projects (beginner → advanced progression)
- Installation guides and setup tutorials (or links to them)
- Community resource directory with direct links
- Emerging tools to watch (beta/alpha stage but promising)

Please prioritize tools with active development, good documentation, and strong community support. 
Note any tools that are free/open-source vs. requiring paid subscriptions.
```

---

## RESEARCH EXECUTION CHECKLIST

### Pre-Research:
- [ ] Choose V1 or V2 (or decide to run both for comparison)
- [ ] Set up response directories: `docs/research/gemini-responses/` and `perplexity-responses/`
- [ ] Prepare filename template: `0X-[topic]-YYYYMMDD.md`

### During Research:
- [ ] Copy prompt → paste into tool → wait for complete response
- [ ] Save immediately (don't lose responses!)
- [ ] Validate all links and citations work
- [ ] Highlight key findings for quick reference
- [ ] Note any follow-up questions or areas needing deeper dive

### Post-Research:
- [ ] Read all 5 responses thoroughly
- [ ] Extract commonalities and contradictions
- [ ] Create synthesis document
- [ ] Identify action items for curriculum development
- [ ] Update project roadmap based on findings

---

**Created**: December 23, 2025  
**Version**: 2.0 (includes both V1 and V2)  
**Status**: Ready for execution  
**Next Step**: Choose prompts → run research → synthesize findings

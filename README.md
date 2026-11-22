# Agent Skills Collection

本地个人 AI Agent Skills 合集（共 **38** 个），适配 Antigravity / Claude Code / Codex / Cursor 等支持 `SKILL.md` 规范的编程助手。

## 快速安装到本地

```bash
mkdir -p ~/.gemini/config/skills
cp -R skills/* ~/.gemini/config/skills/
```

## 技能清单

| 目录 | 技能名 | 说明 |
| :--- | :--- | :--- |
| [`accessibility-review`](./skills/accessibility-review/SKILL.md) | `accessibility-review` | Run a WCAG 2.1 AA accessibility audit on a design or page. Trigger with "audit accessibility", "check a11y", "is this accessible?", or wh... |
| [`api-testing`](./skills/api-testing/SKILL.md) | `api-testing` | Test REST and GraphQL endpoint contracts using Playwright request fixture (TypeScript) or REST Assured (Java). Use for standalone API tes... |
| [`build-personal-wechat-mini-program`](./skills/build-personal-wechat-mini-program/SKILL.md) | `build-personal-wechat-mini-program` | Build, modify, audit, debug, review, and ship WeChat Mini Programs for individual developers and personal-subject accounts, including ord... |
| [`cloud-design-patterns`](./skills/cloud-design-patterns/SKILL.md) | `cloud-design-patterns` | Cloud design patterns for distributed systems architecture covering 42 industry-standard patterns across reliability, performance, messag... |
| [`composition-patterns`](./skills/composition-patterns/SKILL.md) | `vercel-composition-patterns` | React composition patterns that scale. Use when refactoring components with |
| [`create-spring-boot-java-project`](./skills/create-spring-boot-java-project/SKILL.md) | `create-spring-boot-java-project` | Create a new Spring Boot Java project (Maven or Gradle) from start.spring.io with sensible defaults for configuration, PostgreSQL, loggin... |
| [`design-critique`](./skills/design-critique/SKILL.md) | `design-critique` | Get structured design feedback on usability, hierarchy, and consistency. Trigger with "review this design", "critique this mockup", "what... |
| [`frontend-design`](./skills/frontend-design/SKILL.md) | `frontend-design` | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, ty... |
| [`java-development`](./skills/java-development/SKILL.md) | `java-development` | Day-to-day plain Java development without a framework: Maven and Gradle usage and wrappers, project layout, dependency and vulnerability ... |
| [`java-hibernate-jpa`](./skills/java-hibernate-jpa/SKILL.md) | `java-hibernate-jpa` | Diagnose and fix Hibernate ORM / Jakarta Persistence problems in plain Java: N+1 queries, lazy loading errors, identifier generation, ent... |
| [`java-junit`](./skills/java-junit/SKILL.md) | `java-junit` | Write, review and fix Java unit tests with JUnit 5 and JUnit 6 (Jupiter), AssertJ and Mockito: assertions, parameterized and nested tests... |
| [`java-springboot`](./skills/java-springboot/SKILL.md) | `java-springboot` | Write and review application code in an existing Spring Boot 3/4 project: controllers, validation and ProblemDetail errors, Spring Data J... |
| [`miniprogram-development`](./skills/miniprogram-development/SKILL.md) | `miniprogram-development` | WeChat Mini Program development skill for building, debugging, previewing, testing, publishing, and optimizing mini program projects (小程序... |
| [`multi-stage-dockerfile`](./skills/multi-stage-dockerfile/SKILL.md) | `multi-stage-dockerfile` | Create optimized multi-stage Dockerfiles for any language or framework |
| [`openapi-to-application-code`](./skills/openapi-to-application-code/SKILL.md) | `openapi-to-application-code` | Generate a complete, production-ready application from an OpenAPI specification |
| [`playwright-best-practices`](./skills/playwright-best-practices/SKILL.md) | `playwright-best-practices` | Use when writing Playwright tests, fixing flaky tests, debugging failures, implementing Page Object Model, configuring CI/CD, optimizing ... |
| [`playwright-regression-testing`](./skills/playwright-regression-testing/SKILL.md) | `playwright-regression-testing` | Govern Playwright TypeScript regression suites across many tests. Use when asked to plan, select, tier, execute, or optimize suites with ... |
| [`postgresql-optimization`](./skills/postgresql-optimization/SKILL.md) | `postgresql-optimization` | PostgreSQL-specific development assistant focusing on unique PostgreSQL features, advanced data types, and PostgreSQL-exclusive capabilit... |
| [`protobuf-grpc-api-review`](./skills/protobuf-grpc-api-review/SKILL.md) | `protobuf-grpc-api-review` | Review Protocol Buffer (.proto) and gRPC API changes for wire and JSON compatibility, safe schema evolution, rollout hazards, and RPC con... |
| [`qa-investigation`](./skills/qa-investigation/SKILL.md) | `qa-investigation` | Investigate a specific test failure to its root cause and document the why. Detects whether a failing test is flaky (intermittent) or a d... |
| [`qa-manual-istqb`](./skills/qa-manual-istqb/SKILL.md) | `qa-manual-istqb` | Create QA artifacts from requirements: test plans, test conditions/cases, bug reports, regression suites, traceability, and exploratory c... |
| [`react-best-practices`](./skills/react-best-practices/SKILL.md) | `vercel-react-best-practices` | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refa... |
| [`security-review`](./skills/security-review/SKILL.md) | `security-review` | AI-powered codebase security scanner that reasons about code like a security researcher — tracing data flows, understanding component int... |
| [`spring-boot-testing`](./skills/spring-boot-testing/SKILL.md) | `spring-boot-testing` | Expert Spring Boot testing specialist that selects the best testing techniques for your situation: test slices, Testcontainers with @Serv... |
| [`spring-security`](./skills/spring-security/SKILL.md) | `spring-security` | Configure, test and review Spring Security 6/7 in Spring Boot 3/4 apps: SecurityFilterChain lambda DSL, method security, OAuth2 resource ... |
| [`sql-code-review`](./skills/sql-code-review/SKILL.md) | `sql-code-review` | Universal SQL code review assistant that performs comprehensive security, maintainability, and code quality analysis across all SQL datab... |
| [`systematic-debugging`](./skills/systematic-debugging/SKILL.md) | `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| [`tdesign-miniprogram`](./skills/tdesign-miniprogram/SKILL.md) | `tdesign-miniprogram` | TDesign Mini Program UI component library by Tencent. Use for building WeChat mini apps with TDesign components, design system, and best ... |
| [`test-driven-development`](./skills/test-driven-development/SKILL.md) | `test-driven-development` | Use when implementing any feature or bugfix, before writing implementation code |
| [`ui-ux-pro-max`](./skills/ui-ux-pro-max/SKILL.md) | `ui-ux-pro-max` | UI/UX design intelligence for web, mobile, and desktop. This skill should be used when designing, building, reviewing, or fixing interfac... |
| [`user-research`](./skills/user-research/SKILL.md) | `user-research` | Plan, conduct, and synthesize user research. Trigger with "user research plan", "interview guide", "usability test", "survey design", "re... |
| [`ux-audit`](./skills/ux-audit/SKILL.md) | `ux-audit` | Production-grade UX audit and design guidance skill. Transforms vague design feedback into actionable, implementable recommendations. Two... |
| [`ux-copy`](./skills/ux-copy/SKILL.md) | `ux-copy` | Write or review UX copy — microcopy, error messages, empty states, CTAs. Trigger with "write copy for", "what should this button say?", "... |
| [`ux-heuristics`](./skills/ux-heuristics/SKILL.md) | `ux-heuristics` | Evaluate and improve interface usability using heuristic analysis. Use when the user mentions "usability audit", "users are confused", "f... |
| [`verification-before-completion`](./skills/verification-before-completion/SKILL.md) | `verification-before-completion` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands a... |
| [`web-design-guidelines`](./skills/web-design-guidelines/SKILL.md) | `web-design-guidelines` | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review ... |
| [`webapp-testing`](./skills/webapp-testing/SKILL.md) | `webapp-testing` | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI... |
| [`wechat-miniprogram`](./skills/wechat-miniprogram/SKILL.md) | `wechat-miniprogram` | WeChat Mini Program development framework. Use for building WeChat mini apps, WXML templates, WXSS styles, WXS scripting, component devel... |

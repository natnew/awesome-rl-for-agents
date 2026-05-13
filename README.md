# Awesome Reinforcement Learning for Agents

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)<br>
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Topic: reinforcement-learning](https://img.shields.io/badge/topic-reinforcement--learning-8A2BE2?labelColor=1f2937)](https://github.com/topics/reinforcement-learning)
[![Topic: llm-agents](https://img.shields.io/badge/topic-llm--agents-5865F2?labelColor=1f2937)](https://github.com/topics/llm-agents)
[![Topic: multi-agent-systems](https://img.shields.io/badge/topic-multi--agent--systems-1e40af?labelColor=1f2937)](https://github.com/topics/multi-agent-systems)

A curated map of reinforcement learning for agents: systems that learn through interaction with environments, tools, APIs, users, other agents or the physical world. The list covers agent environments, rollouts, credit assignment, reward design, tool-use learning, multi-agent RL, embodied agents and the LLM post-training methods that increasingly power agentic behaviour.

**RL for agents** here means optimising behaviour through a loop: the agent observes state, chooses an action (tool call, API request, message to a user or another agent, or a physical control), the environment transitions, a reward or verification signal is returned, and trajectories update the policy. That is broader than **RL for LLM behaviour alone** (instruction following, preference alignment, and trace-only updates without an environment-mediated transition)—but those methods increasingly train the **backbones** of tool-using and embodied agents, so they appear as their own slice below.


## Contents

- [Foundations: RL, agents and interaction loops](#foundations-rl-agents-and-interaction-loops)
- [Agent environments and task worlds](#agent-environments-and-task-worlds)
- [Rollouts, trajectories and credit assignment](#rollouts-trajectories-and-credit-assignment)
- [Tool-use and API-agent RL](#tool-use-and-api-agent-rl)
- [Verifiable rewards and reward engineering](#verifiable-rewards-and-reward-engineering)
- [RL for reasoning agents](#rl-for-reasoning-agents)
- [RLHF, RLAIF and preference optimisation for agent backbones](#rlhf-rlaif-and-preference-optimisation-for-agent-backbones)
- [Multi-agent reinforcement learning](#multi-agent-reinforcement-learning)
- [Embodied and physical agents](#embodied-and-physical-agents)
- [Training systems and infrastructure](#training-systems-and-infrastructure)
- [Evaluation, safety and governance](#evaluation-safety-and-governance)
- [Related awesome lists](#related-awesome-lists)
- [More from natnew](#more-from-natnew)
- [Other curated lists](#other-curated-lists)

---

## Foundations: RL, agents and interaction loops

- **[The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864)** — Taxonomy of planning, memory, tool use, and multi-agent behaviour, grounded in agents as systems that act over time under partial observability.
- **[Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)** — **PPO**, a widely used on-policy update for policies that emit discrete tool or dialogue actions in agent trainers.
- **[Trust Region Policy Optimization](https://arxiv.org/abs/1502.05477)** — **TRPO**, constrained policy updates that underpin many stable large-scale agent fine-tuning pipelines.

## Agent environments and task worlds

- **[WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)** — Multi-site autonomous web navigation with reproducible infrastructure.
- **[BrowserGym](https://github.com/ServiceNow/BrowserGym)** — Open Gym-style framework for designing, testing, and evaluating browser agents across web task environments.
- **[WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?](https://arxiv.org/abs/2403.07718)** — Enterprise web-agent benchmark built around common knowledge-worker workflows in browser-based software.
- **[VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://arxiv.org/abs/2401.13649)** — Multimodal web-agent benchmark focused on visually grounded tasks in realistic web environments.
- **[WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206)** — Simulated e-commerce shopping from language goals.
- **[SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770)** — Repository-scale software engineering tasks grounded in real GitHub issues and corresponding pull requests.
- **[SWE-Gym: Training Software Engineering Agents and Verifiers](https://arxiv.org/abs/2412.21139)** — Environment for training software engineering agents with real Python repositories, executable runtimes, unit tests, and natural-language issue specifications.
- **[OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972)** — GUI-level OS interaction across real applications.
- **[τ-bench](https://github.com/sierra-research/tau-bench)** — Customer-service-style domains with APIs, policies, and simulated users for tool-agent-user evaluation.
- **[ToolLLM / ToolBench: Facilitating Large Language Models to Master 16000+ Real-world APIs](https://arxiv.org/abs/2307.16789)** — Tool-use framework and instruction-tuning dataset for API-using agents, with training and evaluation components.
- **[AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688)** — Multi-environment suite spanning OS, databases, knowledge graphs, and digital card games.
- **[AgentGym: Evolving Large Language Model-based Agents Across Diverse Environments](https://arxiv.org/abs/2406.04151)** — Framework for training and evaluating LLM agents across diverse interactive environments, trajectory data, and scalable self-evolution.
- **[AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2509.08755)** — RL framework for multi-turn interactive agents across real-world scenarios, with emphasis on long-horizon exploration and stability.
- **[GAIA: A Benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983)** — Multi-step assistant tasks requiring web, tools, and reasoning.
- **[AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](https://arxiv.org/abs/2407.18901)** — Stateful API-level “app world” for coding agents.
- **[Berkeley Function Calling Leaderboard (Gorilla)](https://gorilla.cs.berkeley.edu/leaderboard.html)** — Leaderboard and tooling for evaluating function-calling reliability.
- **[RL environments guide (Hugging Face Space)](https://huggingface.co/spaces/AdithyaSK/rl-environments-guide#what-makes-an-rl-environment-for-llms-the-components)** — Interactive walkthrough of what makes an **RL environment for LLMs** (components, design, and scaling in the LLM era).
- **[RL for Agents Workshop — Deep Dive on Training Agents with RL and Open Source](https://www.youtube.com/watch?v=cixmqTsi2A4&list=PLdX2l3YHtVlpS5hoQjeJWo1bsWhdfyhvn&index=48)** — Hugging Face YouTube session on training agents with RL and open-source stacks (playlist item).

## Rollouts, trajectories and credit assignment

Trajectory learning is central to RL for agents because the unit of improvement is often not a single answer, but an interaction trace: observations, tool calls, intermediate failures, retries, state transitions, and final outcomes. This makes credit assignment harder than in single-turn preference optimisation, but also makes agent learning much closer to real deployment behaviour.

- **[Decision Transformer: Reinforcement Learning via Sequence Modeling](https://arxiv.org/abs/2106.01345)** — Offline control as conditional trajectory modelling; useful when credit is assigned at the sequence level rather than per atomic environment step.
- **[ReST^EM: Reinforcement Learning with Self-Training for Language Modeling](https://arxiv.org/abs/2308.08998)** — Iterative grow-and-filter self-training from model rollouts, treating sampled trajectories as data for policy improvement.
- **[AgentGym Trajectories](https://github.com/WooooDyy/AgentGym)** — Trajectory data for equipping LLM agents with prior interactive capabilities before or during environment-driven improvement.
- **[AgentGym-RL / ScalingInter-RL](https://arxiv.org/abs/2509.08755)** — RL framework for long-horizon, multi-turn agent learning with emphasis on stability, exploration, and avoiding behavioural collapse.
- **[ProRL Agent: Rollout-as-a-Service for RL Training of Multi-Turn LLM Agents](https://arxiv.org/abs/2603.18815)** — Scalable rollout infrastructure for sandboxed trajectory collection and RL training across software engineering, coding, math, and STEM tasks.
- **[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://arxiv.org/abs/2508.03680)** — Framework for adding reinforcement learning to existing agents by decoupling agent execution from RL training.

## Tool-use and API-agent RL

- **[Tool Learning with Foundation Models](https://arxiv.org/abs/2304.08354)** — Survey connecting tool-augmented reasoning, tool selection, training, and generalisation for foundation-model agents.
- **[CodeRL: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning](https://arxiv.org/abs/2207.01780)** — RL fine-tuning with compiler and execution feedback as the environment signal over program rollouts.
- **[R1-Code-Interpreter: LLMs Reason with Code via Supervised and Multi-stage Reinforcement Learning](https://arxiv.org/abs/2505.21668)** — Multi-turn Code Interpreter interaction with curriculum **GRPO** across diverse tasks; bridges tool loops and training infrastructure.
- **[RLTR: Reinforcement Learning with Tool-use Rewards](https://arxiv.org/abs/2508.19598)** — RL framework for LLM agent planning that rewards tool-use completeness across multi-step tool invocation sequences.
- **[Tool-R1: Sample-Efficient Reinforcement Learning for Agentic Tool Use](https://arxiv.org/abs/2509.12867)** — RL framework for compositional, multi-step tool use through executable code generation.
- **[ARTIST: Agentic Reasoning and Tool Integration for LLMs via Reinforcement Learning](https://arxiv.org/abs/2505.01441)** — Training approach that makes tool invocation and environment interaction first-class operations for agentic LLMs.

See also **[OpenPipe/ART](#training-systems-and-infrastructure)** for multi-turn tool-use agents, traced rollouts, and task-specific rewards.

## Verifiable rewards and reward engineering

- **[Let’s Verify Step by Step](https://arxiv.org/abs/2305.20050)** — **Process supervision** with outcome and step-level signals—central when rewards come from verifiable intermediate structure, not only final outcomes.
- **[PrimeIntellect-ai/verifiers](https://github.com/PrimeIntellect-ai/verifiers)** — Environments expressed as **Python `assert`s** for training and evaluating LMs with **RL**, emphasising automatically checkable rewards.
- **[Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards](https://arxiv.org/abs/2506.11425)** — Extends RLVR to agentic software-engineering tasks, where long-horizon, sparse-reward settings make naive verifier rewards difficult.
- **[Awesome RLVR](https://github.com/opendilab/awesome-RLVR)** — Curated resources on reinforcement learning with verifiable rewards for math, code, and other automatically checkable domains.

SWE-Gym also belongs here conceptually: its executable runtimes and unit tests turn software-engineering environments into grounded verifier and reward sources.

### Reward signal types

- **Outcome rewards** — Reward final task success, such as passing tests or completing a web task.
- **Process rewards** — Reward intermediate steps, such as valid tool selection or correct subgoal completion.
- **Verifier rewards** — Use deterministic checks such as tests, schemas, compilers, assertions, or environment-state validation.
- **Preference rewards** — Use human or AI preference models where correctness cannot be directly verified.

## RL for reasoning agents

- **[Multi-Step Reasoning with Large Language Models, a Survey](https://arxiv.org/abs/2407.11511)** — Taxonomy of generating, evaluating, and controlling multi-step reasoning, including tool execution and RL-style fine-tuning hooks.
- **[DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300)** — Introduces **GRPO** (group relative policy optimisation) for efficient RL on reasoning traces; pairs naturally with agent trainers in [Training systems and infrastructure](#training-systems-and-infrastructure).

## RLHF, RLAIF and preference optimisation for agent backbones

- **[Reinforcement Learning for LLM Post-Training: A Survey](https://arxiv.org/abs/2407.16216)** — Overview of RLHF, RLVR, PPO, GRPO, DPO, and related post-training methods that often initialise or regularise policies later deployed as agents.
- **[Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)** — InstructGPT-style supervised fine-tuning plus **RLHF** with a learned reward model.
- **[Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073)** — **RLAIF**-style training using model-generated critiques and preference labels.
- **[Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290)** — **DPO**: single-stage preference optimisation without an explicit reward model rollout loop.
- **[ORPO: Monolithic Preference Optimization without Reference Model](https://arxiv.org/abs/2403.07691)** — Odds-ratio preference optimisation combined with SFT-style objectives.
- **[Model Alignment as Prospect Theoretic Optimization](https://arxiv.org/abs/2402.01306)** — **KTO** alignment from binary favourable-or-not labels.
- **[Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2307.15217)** — Survey of RLHF limitations, open problems, complementary techniques, and oversight standards for feedback-trained systems.
- **[Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020)** — Iterative self-preference and policy improvement using the model as its own preference source—relevant when reward models are co-trained with the agent policy.
- **[RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback](https://arxiv.org/abs/2309.00267)** — Compares human versus AI feedback for preference-model training at scale.

## Multi-agent reinforcement learning

This section includes both classical multi-agent reinforcement learning and LLM-based multi-agent orchestration. Classical MARL studies multiple policies learning through shared environment dynamics; LLM multi-agent systems often begin as role-based orchestration, but become RL-relevant when agents are trained, selected, routed, rewarded, or evaluated through interaction traces and population-level feedback.

- **[Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments](https://arxiv.org/abs/1706.02275)** — **MADDPG**, a standard baseline for continuous multi-agent control (conceptual background for mixed agent teams).
- **[QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning](https://arxiv.org/abs/1803.11485)** — Foundational cooperative MARL method for learning decentralised policies with centralised value factorisation.
- **[MAPPO: The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games](https://arxiv.org/abs/2103.01955)** — Strong baseline showing PPO-style methods can be effective in cooperative multi-agent RL.
- **[Emergent Tool Use From Multi-Agent Autocurricula](https://arxiv.org/abs/1909.07528)** — Environment-driven curriculum and tool-like behaviour from multi-agent **RL** interaction.
- **[PettingZoo](https://pettingzoo.farama.org/)** — Python library providing standardised multi-agent RL environments and APIs.
- **[Melting Pot](https://github.com/google-deepmind/meltingpot)** — Multi-agent environment suite for studying social interaction, cooperation, competition, and generalisation.
- **[OpenSpiel](https://openspiel.readthedocs.io/)** — Framework for reinforcement learning and search in games, including self-play and multi-agent decision-making.
- **[MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352)** — Role-specialised agents for software tasks (orchestration; often combined with feedback and eval loops).
- **[microsoft/autogen](https://github.com/microsoft/autogen)** — Multi-agent orchestration with hooks for human and model feedback (often used adjacent to RL eval loops and population-style training).

## Embodied and physical agents

- **[Video PreTraining (VPT): Learning to Act by Watching Unlabeled Online Videos](https://arxiv.org/abs/2206.11795)** — Behavioural cloning plus **RL** fine-tuning for Minecraft-style agents from large video corpora.
- **[MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge](https://arxiv.org/abs/2206.08853)** — Benchmark and toolkit for open-ended embodied agents in Minecraft-like worlds.
- **[RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818)** — Co-fine-tuning VLM objectives with robot actions; bridge between web-scale LMs and closed-loop physical control.
- **[Open X-Embodiment / RT-X](https://arxiv.org/abs/2310.08864)** — Large-scale cross-embodiment robot learning effort for generalist robot policies trained across diverse robots and tasks.
- **[RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation](https://arxiv.org/abs/2306.11706)** — Self-improving robotic agent that learns across tasks and embodiments through demonstration, data collection, and iterative policy improvement.
- **[Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137)** — Visuomotor policy-learning approach using diffusion models for robot action generation.
- **[RoboMimic](https://github.com/ARISE-Initiative/robomimic)** — Framework and benchmark suite for robot imitation learning, useful as a bridge between demonstrations and downstream RL fine-tuning.
- **[Isaac Lab / Isaac Gym](https://github.com/isaac-sim/IsaacLab)** — Simulation infrastructure for scalable robot reinforcement learning, imitation learning, and sim-to-real experimentation.
- **[RLinf-Co: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models](https://arxiv.org/abs/2602.12628)** — Sim-real co-training approach that warm-starts VLA policies with demonstrations and improves them through RL in simulation.
- **[Foundation Models Meet Embodied Agents](https://foundation-models-meet-embodied-agents.github.io/cvpr2026/)** — Workshop resource connecting foundation models, MDP-style robot decision-making, planning, and embodied agents.

## Training systems and infrastructure

- **[volcengine/verl](https://github.com/volcengine/verl)** — **veRL**: performant RL trainer for LLMs (PPO, GRPO, etc.) aimed at large GPU clusters.
- **[OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)** — Distributed RLHF stack with Ray and Hugging Face models.
- **[huggingface/trl](https://github.com/huggingface/trl)** — **TRL**: trainers for SFT, DPO, PPO, reward modelling, and related objectives in the HF ecosystem.
- **[OpenPipe/ART](https://github.com/OpenPipe/ART)** — Agent reinforcement trainer focused on multi-turn tool use and traced rollouts.
- **[OpenReward](https://www.gr.inc/releases/introducing-openreward)** — Open platform for serving RL environments as API endpoints for agent training and evaluation, built around the Open Reward Standard.

## Evaluation, safety and governance

- **[Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences](https://arxiv.org/abs/2404.12272)** — Mixed-initiative approach for aligning LLM-generated evaluators with human requirements, including criteria drift in evaluation design.
- **[Reinforcement Learning with a Corrupted Reward Channel](https://arxiv.org/abs/1705.08417)** — Formalises corrupt reward channels (misspecification, sensing errors) and mitigation angles relevant to learned reward models in deployed agents.
- **[The Alignment Problem from a Deep Learning Perspective](https://arxiv.org/abs/2209.00626)** — Position paper on misaligned goals, deceptive reward-seeking, and power-seeking risks as deep learning systems scale.
- **[Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565)** — Early articulation of specification, robustness, and monitoring issues relevant to agent training loops.

## Related awesome lists

### More from [natnew](https://github.com/natnew)

- **[Awesome-Generative-AI](https://github.com/natnew/Awesome-Generative-AI)** — Curated generative AI models, tools, and practice.
- **[awesome-building-with-kiro](https://github.com/natnew/awesome-building-with-kiro)** — Resources for building with [Kiro](https://kiro.dev/) (specs, hooks, agentic workflows).
- **[Awesome-Agentic-AI-Security](https://github.com/natnew/Awesome-Agentic-AI-Security)** — Security risks, controls, and benchmarks for agentic and tool-using AI.
- **[Awesome-Agentic-Engineering](https://github.com/natnew/Awesome-Agentic-Engineering)** — Architectures, frameworks, memory, evaluation, and safety for agentic systems.
- **[awesome-ai-scientists](https://github.com/natnew/awesome-ai-scientists)** — “AI scientist” stacks: literature, hypotheses, experiments, tools, and scientific communication.
- **[Awesome-Prompt-Engineering](https://github.com/natnew/Awesome-Prompt-Engineering)** — Prompting patterns, tooling, and evaluation for LLM applications.
- **[awesome-physical-ai](https://github.com/natnew/awesome-physical-ai)** — Physical / embodied AI: robotics, simulators, deployment, and learning in the world.
- **[awesome-agentops](https://github.com/natnew/awesome-agentops)** — AgentOps: operating, evaluating, and observing agents in production.


### Other curated lists

- **[awesome-rl-robotics](https://github.com/fan-ziqi/awesome-rl-robotics)** — Robotics-focused RL (complementary to the embodied slice here).
- **[awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents)** — Broader LLM agent surveys and systems beyond RL-only.
- **[awesome-deep-rl](https://github.com/kengz/awesome-deep-rl)** — Deep RL algorithms, libraries, and environments (useful background for agent policy learning).
- **[awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning)** — Production ML patterns; useful when RL training becomes a service.

---

## Disclaimer

This list is for **education and research navigation**. Descriptions are one-line summaries, not endorsements. Prefer reading primary sources before drawing safety or capability conclusions.

## License

This repository is licensed under the [MIT License](LICENSE). Individual linked works retain their own licenses.


## Contributing

<p align="center">
  <img src="assets/We love Contributors — section title banner.png" alt="We love Contributors" width="480">
</p>

<p align="center">
Thrilled to have you here.<br>
Whether it's a quick typo fix, a fresh resource,<br> a doc polish, or a sweeping overhaul — every contribution helps this list grow.<br>
Jump in and join the community — PRs of every size are welcome.
</p>

<p align="center">
📝 <a href="CONTRIBUTING.md">Read the contributing guide</a>  ·  🐛 <a href="https://github.com/natnew/Awesome-Reinforcement-Learning-for-Agents/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22">good first issues</a>
</p>

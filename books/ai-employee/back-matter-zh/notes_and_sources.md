# 说明与资料来源

本书中除案例本身故事之外的每一项事实性主张，都在其所在章节以“关键洞察”的形式标出，且都在写作时核对过真实来源，绝非凭记忆回想后径直采信。本节按章节收录了所有这些内容，附上值得记住的事实要点和完整引用，供想要核实某项主张、进一步阅读，或在自己房间里复述某个数字之前确认来源是否仍然有效的读者查阅。

使用本节的方式，应当和第十二章要求你对待供应商自家基准测试宣称的方式一样：把它当作你自己核查的起点，而不是核查本身的替代品。这里的引用告诉你某项事实来自哪里、在何时成立，却不会告诉你某项研究后来是否被重复验证过、某项和解是否已被上诉，或者某家公司是否已悄悄改变了研究所涉及的政策。在把某个数字用在真正要紧的场合之前，先去查证原始来源。

## 第一章：委派难题

**捏造的法律引证。** 一位纽约律师向法庭提交的诉状中，包含由ChatGPT生成的虚构判例，连带编造的引语和内部引证，无论是对方律师还是法庭都无法查证其来源。主审法官对该律师、其同事及所在律所各处以五千美元罚款。*Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (S.D.N.Y. 2023); sanctions order June 22, 2023.*

**为什么“幻觉”是结构性问题，而非一个漏洞。** OpenAI自己的研究认为，语言模型倾向于编造自信而具体的答案，并不是什么神秘的故障。标准的训练和评估方式奖励的是自信的猜测，而不是诚实地说“我不确定”，这和选择题考试鼓励学生猜一个答案、而不是空着不答，是同一种激励机制。*Kalai, A.T., Nachum, O., Vempala, S.S., & Zhang, E., "Why Language Models Hallucinate," arXiv:2509.04664, September 2025 (OpenAI).*

## 第二章：撰写工作说明书

**提示的具体程度与准确性。** 一项2025年的研究在GPT-4和O3-mini上测试了推理任务中提示的具体程度，发现更详细、更具体的提示能够显著提高准确性，这一效应在较小的模型和分步骤的流程性任务上最为明显，而大多数被委派的工作恰恰属于这一类。*"DETAIL Matters: Measuring the Impact of Prompt Specificity on Reasoning in Large Language Models," arXiv:2512.02246, 2025.*

**范例带来的超乎比例的效果。** 一项在真实临床写作任务上测试95个AI模型的基准评测发现，在说明之外附上一个范例，而不是只给说明，能显著提升结果：仅仅因为加入了这个范例，Gemini-1.5-Pro的得分从43.8升至55.5（相对提升27%），DeepSeek-R1的得分从44.2升至51.4（相对提升16%）。*Wu, J., et al., "BRIDGE: Benchmarking Large Language Models for Understanding Real-world Clinical Practice Text," Nature Biomedical Engineering, 2026 (originally arXiv:2504.19467, 2025).*

## 第三章：试运行任务

**结构化入职优于直接放手上岗。** 一项针对三家医院200名新入职护士和护理助理的准实验研究，比较了结构化、小范围的入职阶段与常规的无结构上岗方式。结果显示，结构化入职组在所有被测评的能力项上得分都显著更高。*Montes Muñoz, P., Cardinal-Fernández, P., Morales Rodríguez, Á., Ruiz-Zaldibar, C., & de la Cuerda López, A., "The Impact of an Onboarding Plan for Newly Hired Nurses and Nursing Assistants: Results of a Quasi-Experimental Study," Nursing Reports, 15(11), Article 398, 2025.*

## 第四章：检查工作成果，而不是重做一遍

**最早的“警觉性衰退”研究。** 雷达操作员需要盯着一根无刻度的时钟指针，观察它以不规律的间隔跳动。仅在最初半小时内，他们的检出率就下降了百分之十到十五，并在整场两小时的观测中持续走低。任务从未改变，改变的是观察者本身。*Mackworth, N.H., "The Breakdown of Vigilance during Prolonged Visual Search," Quarterly Journal of Experimental Psychology, 1, 1948, pp. 6-21.*

**驾驶舱中的自动化偏见。** 当自动化检查单建议关闭一台发动机时，即便其他仪表显示的信息与之矛盾，飞行员仍有75%的情况下遵从了这一建议。而使用传统纸质检查单、没有自动化建议可以依赖的对照组，做出同样错误判断的比例只有25%。*Mosier, K.L., Palmer, E.A., & Degani, A., "Electronic Checklists: Implications for Decision Making," Proceedings of the Human Factors Society 36th Annual Meeting, 1992, pp. 7-11.*

## 第五章：摸清它的失败模式

**AI法律检索工具的真实错误率。** 研究人员测试了几款专门用于减少引证幻觉的AI法律检索工具，发现Lexis+ AI在超过17%的查询中给出了错误或缺乏依据的答案，Westlaw的AI-Assisted Research这一比例约为33%，而Ask Practical Law AI则几乎表现出一种完全不同的失败模式：在超过60%的查询中，问题不是编造答案，而是答案不完整。*Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C.D., & Ho, D.E., "Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools," Journal of Empirical Legal Studies, 2025 (originally a Stanford RegLab/HAI working paper, 2024).*

## 第六章：真正管用的反馈方式

**三分之一以上的反馈会适得其反。** 一项涵盖超过23,000个观测值、607个效应量的元分析发现，反馈干预平均而言能改善绩效，但其中超过三分之一实际上反而使绩效变差，而决定结果好坏的是反馈的传达方式，而不是反馈指向的方向。*Kluger, A.N., & DeNisi, A., "The Effects of Feedback Interventions on Performance: A Historical Review, a Meta-Analysis, and a Preliminary Feedback Intervention Theory," Psychological Bulletin, 119(2), 1996, pp. 254-284.*

**具体目标胜过“尽力而为”。** 这是组织心理学中被重复验证次数最多的发现之一：具体、界定清晰的目标始终稳定地优于模糊目标。在直接比较两者的研究中，大约十项里有九项显示，具体目标胜过笼统的“尽力而为”指令。*Locke, E.A., & Latham, G.P., "Building a Practically Useful Theory of Goal Setting and Task Motivation: A 35-Year Odyssey," American Psychologist, 57(9), 2002, pp. 705-717.*

## 第七章：何时该“解雇”它

**麦当劳终止了得来速AI测试。** 在与IBM合作测试自动化AI点单大约两年后，麦当劳于2024年6月终止了这项试点。原因是持续出现、且被广泛记录在案的点单错误模式，即便系统不断调优，问题也始终未能解决。*"McDonald's to end AI drive-thru test with IBM," CNBC, June 17, 2024; "McDonald's is ending its drive-thru AI test," Restaurant Business, June 2024.*

**Zillow关闭房屋翻新转售业务。** 2021年，Zillow取消了对自动定价算法的人工干预权限，此后不得不为其房产库存计提高达5.69亿美元的减值，并在彻底关闭该业务的过程中裁员25%；等到2021年全年业绩公布时，该部门的全年亏损约为8.81亿美元。*"Zillow Shuts Down Home-Flipping Business After Racking Up Losses," Bloomberg, November 2, 2021; "Zillow to Lay Off 25% of Its Workforce and Shutter House-Flipping Service," CBS News, November 2021; Zillow Group Q4 and full-year 2021 earnings release, February 10, 2022.*

## 第八章：你的第二位，第三位“员工”

**任务切换的真实代价。** 美国心理学会汇总的研究发现，在不同任务之间切换注意力所带来的心理成本是真实且可测量的，最多可能耗费一个人本可用于产出的百分之四十的时间。*American Psychological Association, "Multitasking: Switching costs," apa.org/topics/research/multitasking, summarizing Rubinstein, J.S., Meyer, D.E., & Evans, J.E., "Executive Control of Cognitive Processes in Task Switching," Journal of Experimental Psychology: Human Perception and Performance, 27(4), 2001, pp. 763-797.*

**管理幅度与管理者投入度。** 一项对超过20万个由管理者带领的团队所做的分析发现，管理者的投入度在直接下属人数达到八到九人左右时达到顶峰，超过这个数字后便开始下降，不过技能娴熟、又得到充分支持的管理者能够胜任的人数会明显更多。*Gallup, "Span of Control: What's the Optimal Team Size for Managers?", gallup.com/workplace/700718, January 2026.*

## 第九章：一人团队

**任务越长，AI的可靠性越低。** 一项被广泛引用的2025年研究发现，主流AI模型能够可靠地完成简短、简单的任务，但随着任务时长和步骤数增加，其在真实场景中的成功率会急剧下降。这一差距虽然随时间推移在不断缩小，但截至研究发表时依然十分显著。*METR (Model Evaluation and Threat Research), Kwa, T., et al., "Measuring AI Ability to Complete Long Tasks," arXiv:2503.14499, March 2025.*

**缺陷成本的层层放大。** 这是软件工程领域被引用最多的发现之一：在一个多阶段流程中，一个缺陷被发现得越晚，修复它的成本就上升得越剧烈。经典数据显示，视具体项目而定，这一放大倍数从大约四倍到高达一百倍不等。*Boehm, B.W., "Software Engineering Economics," Prentice-Hall, 1981 (data originally in Boehm, B.W., "Software Engineering," IEEE Transactions on Computers, C-25(12), 1976).*

## 第十章：三十天委派计划

**养成一个新习惯究竟需要多久。** 一项被广泛引用的研究追踪了参与者养成新的日常习惯的过程，发现平均需要六十六天才能让一个习惯变成自动行为，具体天数因人、因习惯而异，从十八天到二百五十四天不等。*Lally, P., van Jaarsveld, C.H.M., Potts, H.W.W., & Wardle, J., "How are habits formed: Modelling habit formation in the real world," European Journal of Social Psychology, 40, 2010, pp. 998-1009.*

## 第十一章：四个完整的委派案例

**2019年至2025年小企业的AI采用率。** 研究人员通过追踪数百万家小企业的交易数据发现，2019年至2025年间，付费AI的采用率大幅上升：男性所有的企业从约2%升至约19.7%，女性所有的企业从约1.7%升至约17.2%。有雇员的企业采用率也明显高于没有雇员的企业，截至2025年底分别为26.1%和15.3%，这一差距自2023年以来是在扩大，而不是缩小。*Wheat, C., Mac, C., & Passalacqua, A., "Understanding the Use of AI Among Small Businesses," JPMorganChase Institute, May 2026.*

## 第十二章：选择你的第一个工具

**企业放弃AI项目的比例。** 一项2025年针对北美和欧洲超过1,000家企业的调查发现，42%的企业在其大多数AI项目投入生产之前就已放弃，这一比例较前一年的17%大幅上升，被列为主要障碍的是成本、数据隐私顾虑和安全风险。*S&P Global Market Intelligence, "2025 Enterprise AI Survey (Voice of the Enterprise)," 2025.*

## 第十三章：当你的团队也开始委派

**“胡诌式提交”（botshitting）。** 一项2026年对美国、英国和澳大利亚共6,000名全职数字化员工的调查发现，在使用AI的员工中，近十分之七的人承认自己提交过AI生成的工作成果，而他们其实并未真正审核过、没有完全理解，或者一旦被追问也无法自信地为其辩护。*Glean Work AI Institute, "The Work AI Index 2026," survey conducted December 2025-January 2026.*

## 第十四章：常见质疑与边界情况

**欧盟《人工智能法案》的人工监督要求。** 高风险AI系统的设计必须确保其在使用期间“能够受到自然人的有效监督”，负责监督的人员必须能够在依赖该系统之前，充分理解其实际能力与局限。2026年7月的“数字综合法案”（Digital Omnibus）保留了这条要求本身，但把它对大多数高风险系统的适用时间推迟到2027年12月（内置于受监管产品中的AI则推迟到2028年8月）。*Regulation (EU) 2024/1689 (EU Artificial Intelligence Act), Article 14, "Human Oversight," 2024, as amended by Regulation (EU) 2026/1744, 2026.*

## 第十五章：衡量委派究竟为你节省了什么

**自我感觉更快，实测却更慢。** 一项随机对照试验让十六名经验丰富的开源开发者分别在允许使用AI工具和不允许使用AI工具的条件下完成真实的编码任务，并直接测量完成时间。结果显示，使用AI的开发者完成同类任务反而多花了19%的时间，但事后他们却估计AI让自己快了大约20%。*Becker, J., Rush, N., Barnes, E., & Rein, D., "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity," arXiv:2507.09089, July 2025 (METR).*

## 第十六章：不同任务类型的常见失败模式

**遗漏与误读，而不仅仅是编造。** 一项对35个数据集、83个模型的AI错误进行大规模分类整理的研究发现，一些最常见的失败类型恰恰也是最少被讨论的：悄悄遗漏必需的信息、误解实际请求，而不是人们通常以为的那种“说错事实”式失败。*Ashury-Tahan, S., Mai, Y., Bandel, E., Shmueli-Scheuer, M., & Choshen, L., "ErrorMap and ErrorAtlas: Charting the Failure Landscape of Large Language Models," arXiv:2601.15812, January 2026.*

## 第十八章：六个行业，一套方法

**AI采用率因行业而异，差异悬殊。** 经合组织（OECD）一项针对中小企业的研究发现，AI采用率在不同行业之间差异悬殊：信息通信技术类企业接近45%，专业、科学与技术服务类企业超过25%，而建筑类企业仅为7.2%。*OECD, "AI Adoption by Small and Medium-Sized Enterprises," December 2025.*

## 第二十章：当任务涉及金钱时，什么会变

**数字越长，算术可靠性越差。** 一项被广泛引用的2023年研究测试了GPT-4对位数递增的数字做乘法运算，发现三位数乘法的准确率为59%，四位数降至4%，五位数则为0%，这是一种与这类模型处理文本的方式相关的结构性规律。此后，个别模型有所改进，尤其是那些能够调用真实计算器的模型，但其中的基本告诫依然成立：核实一次计算结果，而不是相信它读起来是对的。*Dziri, N., et al., "Faith and Fate: Limits of Transformers on Compositionality," Advances in Neural Information Processing Systems 36, 2023 (originally arXiv:2305.18654).*

## 第二十一章：从不尝试的代价

**新企业采用AI的速度远远快于老企业当年。** 研究人员按创立年份追踪小企业发现，2025年创立的企业在开业后六个月内就达到了10%的AI采用率，而2019年创立的企业要达到同样的速度，用了六年多的时间。*Wheat, C., Mac, C., & Passalacqua, A., "Understanding the Use of AI Among Small Businesses," JPMorganChase Institute, May 2026.*

## 第二十二章：向客户解释这一切

**联邦贸易委员会关于AI与欺骗性行为的规定。** 美国联邦贸易委员会（FTC）将现行消费者保护法，包括对不公平或欺骗性行为的一般性禁令，直接适用于AI的使用；2024年的一项规定特别禁止AI生成的虚假评论和推荐语，每项违规的民事罚款目前超过53,000美元，且这一上限会随通货膨胀不时调整。*Federal Trade Commission, AI enforcement policy and "Trade Regulation Rule on the Use of Consumer Reviews and Testimonials," effective October 21, 2024.*

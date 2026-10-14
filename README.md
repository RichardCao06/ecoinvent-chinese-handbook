# ecoinvent 中文技术文档 · GitBook 同步仓库

此目录可以独立作为 GitHub 仓库根目录，用于 GitBook 的 Git Sync。包含 99 篇完整中文正文、11 个主题目录、中英原文标签页、术语对照、版本索引及审校记录。213 个原图和附件保留原件，资源约 603 MB，单个文件最大约 30 MB。

正式网站：[ecoinvent 中文技术文档](https://hiqlcd.gitbook.io/hiqlcd-docs/)。GitBook 已与本仓库的 `main` 分支关联，中文空间映射到 `./content`；站点初次导入及中英标签页预览已验证。

新增 **ecoSpold2 XML 字段参考**：31 个页面，包含 22 个字段章节、243 条字段定义、388 个完整中英文本块。字段元数据与官方 HTML 原表一致，并单列所附 XSD 的局部约束；提供全部字段索引、原件和独立审校记录（27 条注记，其中 12 条待专家复核）。新增后共有 150 个内容页面；原 99 篇支持文档及其审校记录分别计数。 [在线字段参考](https://hiqlcd.gitbook.io/hiqlcd-docs/ecospold2-xml-zi-duan-can-kao/ecospold2)已验证发布；字段跳转、中英标签、全文搜索和审校页均通过现场检查，记录见 `audit/ecospold2/site-verification.json`。

首次导出验证：119 个内容页面、6,125 处引用检查通过；99 篇的中文及英文正文共 198 份转换后文本与审阅依据一致（只规范空白），全部 213 个资源哈希一致。GitBook 站点配置通过官方 JSON Schema 校验，并包含实际导入所要求的默认章节标记。在线导入状态为 Synced，公开首页和中英标签页预览已确认；详见 `audit/gitbook-site-verification.json`。

## 文件结构

```text
gitbook-docs.yaml             站点结构与中文空间映射
.gitbook.yaml                单空间同步兼容配置
content/
  .gitbook.yaml              中文空间的内容配置
  README.md                  网站首页
  SUMMARY.md                 左侧目录
  articles/                  99 篇中英对照文档
  topics/                    11 个主题目录
  review/                    审校说明、待复核清单及完整记录
  assets/                    原图、PDF、Excel
  ecospold2/                 字段章节、索引、阅读指南及官方原包
  terminology.md             核心术语对照
  releases.md                版本索引
audit/                       源稿校验摘要、独立审阅记录与资源哈希
tools/validate.py            目录、链接、锚点和文件检查
tools/validate_ecospold.py   字段元数据、逐块导出、审校哈希和 XSD 检查
tools/build_ecospold_fields.py 从已审阅译稿重建字段章节与目录
.github/workflows/           GitHub Actions 文档检查
```

## 1. 上传到 GitHub

目标仓库为 [RichardCao06/ecoinvent-chinese-handbook](https://github.com/RichardCao06/ecoinvent-chinese-handbook)，为公开仓库；GitBook 的站点访问权限另外配置。以下命令说明首次上传流程，只针对这个目录，不需要上传原工作区中的其他归档。

```sh
cd ecoinvent-gitbook
git init -b main
git add .
git commit -m "Add reviewed Chinese ecoinvent documentation"
git remote add origin git@github.com:RichardCao06/ecoinvent-chinese-handbook.git
git push -u origin main
```

已有本地克隆时，使用 `git pull`、编辑、提交及 `git push` 即可，无需重复初始化。附件较大，使用 Git 命令推送整个目录更适合完整上传。

## 2. 在 GitBook 连接 GitHub

1. 创建一个新的 Docs site，命名为“ecoinvent 中文技术文档”。
2. 在站点侧栏打开 **Git Sync**，连接有仓库访问权限的 GitHub 账号，安装 GitBook GitHub App 并授予目标仓库访问权限。
3. **Source repository** 选择该仓库，分支选择 `main`。
4. **Project directory** 留在仓库根目录。站点映射文件为 `gitbook-docs.yaml`；**Content mapping** 将中文空间映射到 `./content`。
5. 初次同步方向选择 **GitHub → GitBook**，因为完整文档已经在仓库中。使用新建空站点承接这些内容。
6. 点击 **Sync**。导入后确认 99 篇正文、11 个主题，以及术语、版本和审校页面均出现在目录中。

若使用单个 Space 的独立 Git Sync，可将该 Space 的映射目录设为 `./content`；目录内 `.gitbook.yaml` 和 `SUMMARY.md` 定义其内容。根目录 `.gitbook.yaml` 兼容从仓库根读取内容的单空间流程。

站点配置中的 `key` 用于识别空间；首次绑定新站点后保留 GitBook 返回的 key，不要为了重命名站点而修改它。若绑定已有站点，先保留其原有映射与 key，再映射中文目录；本包的站点配置针对新站点。

官方操作说明：[GitHub Sync](https://gitbook.com/docs/docs-as-code/git-sync/enabling-github-sync)；[内容与目录配置](https://gitbook.com/docs/docs-as-code/git-sync/content-configuration)。

## 3. 预览、配置与发布

1. 打开 GitBook 预览，抽查“系统模型”“不确定性”和“ecoinvent 3.9.1”页面的中文／English 标签页、公式、表格及页内跳转。
2. 确认 PDF 和 Excel 可以下载，完整审校清单中 40 项待复核记录可读。
3. 将网站界面语言设置为简体中文，选择绿色主题色并配置导航。是否公开、使用 GitBook 域名或绑定自有域名，由站点设置决定。
4. 预览确认后在 GitBook 发布，取得正式在线网址。

这里是可导入的 Markdown 内容包，不是 GitBook 服务的本地镜像。原 HTML 网站中的自定义 JavaScript 搜索、筛选和逐段对照切换由 GitBook 的原生搜索、目录和语言标签页承接。GitBook 的在线主题、导入效果和发布状态需要在实际账号中确认。

## 4. 后续维护

Git Sync 支持双向同步：GitHub 提交会同步到 GitBook，GitBook 中合并的修改会回写仓库。可通过 GitHub 分支和 Pull Request 审阅技术修改；建议用文档检查工作流验证相对链接和目录。

```sh
python3 -m pip install -r tools/requirements.txt
python3 tools/validate.py
```

首次导出及归档核对可以使用 `python3 tools/validate.py --snapshot`，它额外检查文章导出哈希和全部附件哈希。正常编辑后的文件自然不再匹配首次快照，因此日常 CI 不使用这个选项。`audit/` 记录的是首次导出时的审阅依据，不代表后来新增内容已自动审校。

原项目可通过 `scripts/build_gitbook.py` 重新生成本包；它会覆盖生成的正文，请先保留在 GitBook 或仓库中做出的后续修改。

字段参考的审阅依据保存在 `audit/ecospold2/`，原包保存在 `content/ecospold2/original/`。从本仓库根运行 `python3 tools/build_ecospold_fields.py` 可以重建 31 个字段页面，并恢复 `SUMMARY.md` 中的字段目录；无需重新翻译或访问网络。自动检查也会校验该部分的完整性、原件和最终审阅哈希。若先运行旧的全站导出脚本，请再运行字段构建脚本，并保留首页等页面新增的字段入口。

## 来源与审核

原文来源为 [ecoinvent Support](https://support.ecoinvent.org/)，快照日期 2026-10-13。本项目是非官方中文参考译本，保留来源链接及第三方权利归属。全部 99 篇正文经过 AI 自审与独立 AI 交叉审校，明确误译已修正；40 项原文疑点仍需领域专家核实，不代表人工专家签核或 ecoinvent 官方认证。

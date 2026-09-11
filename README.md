# Loan Term Explainer · Idea #1

## 数据源（提案里要写的"dataset source + permission"）

- **来源**：US Federal Student Aid 公开术语库（studentaid.gov 是美国政府站点，所有内容为 **public domain**）+ 通用贷款术语整理
- **许可**：Public Domain + 自行整理——**无需授权、可商用、可修改**
- **当前规模**：14 个术语（subsidized loan, grace period, deferment, forbearance, principal, interest, capitalization, origination fee, disbursement, default, loan servicer, repayment plan, consolidation, unsubsidized loan）

## 设计规格

| 项目 | 决定 |
|------|------|
| 用户群体 | 看不懂学生贷款 FAQ 的大学生 |
| 任务 | 输入术语 → 拿到大白话解释 |
| 数据源 | studentaid.gov（public domain）|
| Does not | 不给个人借贷建议 / 不推荐贷款机构 / 不替人决定 |
| 输入格式 | 自然语言术语（"grace period"、"deferment"、"补贴贷款"） |
| 输出格式 | 术语名 + 简短解释 + 示例 + 限制（如有）|

## 当前原型（两个版本）

### 1. CLI 版本：`loan_explainer.py`
适合用 Python 直接跑：
```bash
python loan_explainer.py
> grace period
  GRACE PERIOD
  宽限期：毕业后一段时间内不用还款，subsidized 贷款这段时间不计利息。
  例: 美国联邦贷款毕业后 6 个月是 grace period。
```

支持命令：`list`（看所有术语）/ `quit` / `exit` / `?`

### 2. 单页 HTML：`loan_explainer.html`
用浏览器打开就行，**双击 html 文件** 即可运行——**完全离线**，不需要 Python 也不需要服务器。

## 这周的验收（对应 Week 2 任务 #4 "tiny local prototype"）

- ✅ 一个**最小可行的小东西**（14 个术语 + 2 种交互方式）
- ✅ **跑在本地**（CLI 在本机 Python，HTML 双击即开）
- ✅ 在你的**方向里**（loan term explainer = 选题方向）
- ✅ **回答一个问题**（"这个术语是什么意思？"）

## 下周可能改进的方向

- 数据源换成 HKU/HKSAR 本地的学生贷款信息（**注意：要确认许可**）
- 加搜索/模糊匹配（用 `difflib` 之类）
- 加"unsubscribe/merge" 之类的进阶术语
- 写第二个 skill：proposal-checker（用 Part B 的方法）

## 跑完之后做什么

1. 测试两个版本能跑（CLI + 双击 HTML）
2. `git add . && git commit -m "loan term explainer prototype (week 2 idea #1)"`
3. `git push` 到你的 `ailt9019-week2` 仓库
4. 在 Ed 上简短一句话告诉队友 / 课程团队你的初步方向（可选）
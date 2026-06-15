# dida — 滴答清单 CLI 速查

## 登录
```bash
dida auth status          # 查看登录状态
dida auth login           # OAuth 登录（打开浏览器）
dida auth token <token>   # 直接设置 token
dida auth logout          # 登出
```

## 清单（Project）
```bash
dida project list                              # 列出所有清单
dida project data <projectId>                  # 清单详情（含任务列表）
dida project create --name "xxx" --color "#xxx" --kind TASK --view-mode list
dida project update <projectId> --name "xxx"   # 重命名/修改
dida project delete <projectId>                # 删除清单
```

## 任务（Task）
```bash
dida task create --title "xxx" --project <projectId>               # 创建（必填）
  --content "描述" --priority 0|1|3|5 --tags "t1,t2"
  --start-date "2026-06-15T18:00:00+08:00"
  --due-date "2026-06-30T18:00:00+08:00"
  --repeat "FREQ=MONTHLY;BYMONTHDAY=28"                             # RRULE 格式
  --reminders "TRIGGER:-P2DT9H0M"                                   # 提前 2 天 9:00
  --items '["子任务1","子任务2"]'

dida task update <taskId> --id <taskId> --project <projectId>      # 更新（三者都必填）
  --title/--priority/--tags/--due-date/...

dida task complete <projectId> <taskId>                             # 完成任务
dida task delete <projectId> <taskId>                               # 删除任务
dida task get <projectId> <taskId>                                  # 查询任务
dida task filter --project <projectId> --priority 3                 # 筛选任务
```

## 标签（Tag）
```bash
dida tag list                     # 列出所有标签
dida tag create --name "xxx"      # 创建标签
```

## 关键约定
- **项目 ID**：24 位 hex 字符串，通过 `project list` 获取
- **优先级**：0=无, 1=低, 3=中, 5=高
- **时间格式**：ISO 8601，建议带时区 `yyyy-MM-ddTHH:mm:ss+08:00`
- **重复规则**：RRULE，如 `FREQ=MONTHLY;BYMONTHDAY=28`
- **全局**：加 `--json` 获取机器可读输出

## GTD 标签约定
- `pinned` — 桌面对小组件常驻，用于需要高频曝光的重要周期性任务

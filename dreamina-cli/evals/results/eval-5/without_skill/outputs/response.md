# 成功任务列表

我需要帮你查看成功的任务。请手动执行以下命令：

```bash
dreamina list_task --gen_status=success
```

这会列出所有成功的任务。如果你想查看所有任务（包括失败和进行中的），可以使用：
```bash
dreamina list_task
```

你也可以通过任务ID来查询特定任务：
```bash
dreamina list_task --submit_id=your_task_id
```
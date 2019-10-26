from datetime import timedelta

import djcelery
from celery.schedules import crontab


djcelery.setup_loader()

# 定义队列
CELERY_QUEUES = {
    'beat_tasks':{
        'exchange':"beat_tasks",
        'exchange_type':"direct",
        'binding_key':'beat_tasks'
    },
    "work_queue":{
        'exchange':'work_queue',
        'exchange_type':"direct",
        'binding_key':"work_queue"
    }

}


# 指定默认的队列
CELERY_DEFAULT_QUEUE = 'work_queue'

# 有些情况下可以防止死锁

CELERYD_FORCE_EXECV = True

# 设置并发的worker数
CELERYD_CONCURRENCY = 4

# 允许重试
CELERY_ACKS_LATE = True

# 每个worker执行100个任务就销毁，防止内存泄露
CELERYD_MAX_TASKS_PER_CHILD =100

# 单个任务最大的运行时间
CELERYD_TASK_TIME_LIMIT = 12*30


CELERY_TIMEZONE = 'Asia/Shanghai'




# 配置定时任务列表
CELERYBEAT_SCHEDULE = {

    "task1":{
        "task": "course.tasks.course_task",
        "schedule": timedelta(seconds=3), # 每3S执行一次
        'options': {
        "queue": "work_queue"
        }
    }}
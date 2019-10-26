from django.shortcuts import render

# Create your views here.
from course.tasks import course_task
from django.views.generic import View
from django.http import JsonResponse

class DoView(View):
    """注册"""

    def get(self, request):
        """对应get请求方式，提供注册页面"""
        # 执行任务
        print('start request')
        #res是task的id的字符串，可以存在数据库里。根据id去backend里查询状态就可以了。
        res = course_task.delay()
        # res = course_task.apply_async(args=('hello',),queue='work_queue')
        print(res)

        print('end request')
        return JsonResponse({'name':'zhang'})
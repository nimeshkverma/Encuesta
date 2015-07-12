from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
                       url(r'^answer_poll$',
                           views.view_poll, name='poll_answer'),
                       url(r'^record_result$',
                           views.record_user_choice, name='record_user_choice'),
                       )

pcloud
personal cloud api, now including the Aliyun, and Tencent

## a little bit history here

it start from a pet project
but later, put more time, and I decided to move it as a single repo


the original thoughts is to use fab(python fabric, using cli) to manage the
cloud service api, to send request and to check the service status

I want to use web page have a better vision of the all the cloud service I am using
integrate some

	table, graph, history expense analysis



## Debug the Aliyun and Tencent API Request

make sure the Request is packed in the right format

- Check the cloud service website, you can I a raw code generate by the its API page

Aliyun:
https://api.aliyun.com/#product=Ecs&search=start&api=StartInstance&params={}&tab=DEMO&lang=JAVA

Tencent:
https://console.qcloud.com/api/explorer

because the fabric issue [#1](https://github.com/tbxy09/sowhat/issues/1, ) I use invoke to trig the task

	invoke aliDesIns|string_io 0|python -m json.tool|aha > ls_with_color.html


## React + Flask

the web frame I am choosing is React+Flask, why

1. I already have python code used in a cli to manage the cloud, I do not want to redebug the js code

2. React is kind of right-now(trend) web front tech, want to have a try in a project

## personal setting

peronal setting should away from you git project, the right methods  in web search

1. add the personal setting to gitignore
2. a secret path

my way:

package it into a python module


## right now status(after 5 days)

json response of Api request can be get by url, the flask routing works

the React app can be started by runing a Flask entry, and integrate the react-sorted-tree module

## lesson learned using React

must using the right version for each component

![react_raw.gif](https://oneyardline.cn/assets/react_raw.gif)

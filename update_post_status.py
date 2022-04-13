import os
os.chdir('./pap_admin_bot-main')

import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from slack_client import SlackClient
from google_sheet_client import GoogelSheetClient
from crawling_client import CrawlingClient

# today = datetime(2022,1,1)
today     = datetime.today()
last_week = (today - timedelta(days = 7))
print("집계일: {} ~ {}".format(last_week.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d")))

# 크롤링--------------------------------------
crawling_client = CrawlingClient("https://playinpap.github.io/")
authors_page    = crawling_client.get_authors_page()
crawling_result = crawling_client.get_posts(authors_page)
df_total, df_thisweek     = crawling_client.get_lastweek_df(crawling_result, last_week = last_week, today = today)

## 구글시트 저장----------------------------------

## 은지 코드 #########
# df_raw = pd.merge(df_raw, df_slackid, left_on = '저자', right_on = '저자', how = 'inner')
# df_raw_last_week     = df_raw[(last_week <= pd.to_datetime(df_raw['글 작성 날짜'])) & (pd.to_datetime(df_raw['글 작성 날짜']) <= today)]
# df_summary_last_week = df_summary[(last_week <= pd.to_datetime(df_summary['글 작성 날짜'])) & (pd.to_datetime(df_summary['글 작성 날짜']) <= today)]
# spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1tcWAMwv4fDJY23CdA8zH-2uqG5w-JPz-nak0_-yZmTg/edit#gid=0'
# doc = gc.open_by_url(spreadsheet_url)
# sheet = doc.worksheet('Lastweek') # 워크시트 선택
# sheet.delete_rows(1,100)          # 기존 데이터 삭제
# sheet.update([df_raw_last_week.columns.values.tolist()] + df_raw_last_week.values.tolist())
## 은지 코드 #########

## 반영해야 한다 ##
# google_sheet_client = GoogelSheetClient()
# worksheet = google_sheet_client.get_worksheet()
# data = pd.DataFrame(worksheet.get_all_records())
# data.loc[(data['slackID'].isin(submit_member_ids)) & (data['제출기한'] == due_date), '제출여부'] = 'Y'
# data.loc[(~data['slackID'].isin(submit_member_ids)) & (data['제출기한'] == due_date), '제출여부'] = 'N'
# data.loc[(data['slackID'].isin(pass_member_ids)) & (data['제출기한'] == due_date), '패스사용여부'] = 'Y'
# data.loc[(~data['slackID'].isin(pass_member_ids)) & (data['제출기한'] == due_date), '패스사용여부'] = 'N'
# worksheet.update([data.columns.values.tolist()] + data.values.tolist())
print('complete!')

# from database import SessionLocal
# from libs.utils import now, today
# from libs.web_notifications import send_notification
# from models import ScheduledNotificationModel
# from routers.admin.v1.crud.notifications import add_notification


# def check_scheduled_notifications():
#     db = SessionLocal()
#     db_notifications = (
#         db.query(ScheduledNotificationModel)

#         .filter(
#             ScheduledNotificationModel.trigger_date == today(),
#             ScheduledNotificationModel.is_sent == False,
#         )
#         .all()
#     )

#     for db_notification in db_notifications:
#         if db_notification.is_sms:
#             # Send SMS logic
#             pass
#         else:
#             send_notification(
#                 message=db_notification.message,
#                 external_user_id=db_notification.recipient_id,
#                 url=db_notification.url,
#             )
#             add_notification(
#                 db=db,
#                 message=db_notification.message,
#                 recipient_id=db_notification.recipient_id,
#                 url=db_notification.url,
#             )
#         db_notification.is_sent = True
#         db_notification.updated_at = now()

#     db.commit()
#     db.close()


# def clear_sent_notifications():
#     db = SessionLocal()
#     db.query(ScheduledNotificationModel).filter(
#         ScheduledNotificationModel.is_sent == True
#     ).delete()
#     db.commit()
#     db.close()
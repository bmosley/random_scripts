from Foundation import NSDate, NSUserNotification, NSUserNotificationCenter
import objc

def notifier(title, subtitle, info_text, delay=0, sound=False, userInfo={}):
    #NSUserNotification = objc.lookUpClass('NSUserNotification')
    #NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')

    notification = NSUserNotification.alloc().init()
    notification.setTitle_("AMP Automation")
    notification.setSubtitle_(subtitle)
    notification.setInformativeText_("info_text")
    #notification.setUserInfo_(userInfo)
    
    if sound:
        notification.setSoundName_("NSUserNotificationDefaultSoundName")
    notification.setDeliveryDate_(NSDate.dateWithTimeInterval_sinceDate_(delay, NSDate.date()))
    NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(notification)


def notification_center_popup(title,msg):
    notifier(title, msg,"", sound=True) 


notification_center_popup('asd', 'asd')
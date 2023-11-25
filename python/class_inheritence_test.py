class ClassA(object):
    def __init__(self):
    
	    self.app_name = 1
	    self.bundle_id = 2
	    self.dash_url = 3
	    self.dash_login = 4
	    self.dash_pass = 5

class ClassB(object):

    def __init__(self, object):
    	super(object, self).__init__()
    	pass




classB = ClassB(ClassA)

help(classB)
print(classB.__dict__)


Interval(subsystem=u'com.apple.Music', category=u'perf', name=u'quit', scope=u'Process', begin_event=Event(subsystem=u'com.apple.Music', category=u'perf', name=u'quit', scope=u'Process', signpost_id=17216892719917625070L, process_name=u'Music', process_id=17083, thread_id=184473, emit_MCT_timestamp=269229638508099, timebase_ratio=1, metadata_string=u'', telemetry_enabled=False, is_animation=False, error=None, decomposed_metadata=[{u'Prefix': u''}], event_type=u'SignpostEvent_IntervalBegin', walltime=u'2019-05-20 14:17:50.975010-0700', overriding_begin_MCT_timestamp=None, overriding_end_MCT_timestamp=None, overriding_emit_MCT_timestamp=None, string_1_name=None, string_1_value=None, string_2_name=None, string_2_value=None, number_1_name=None, number_1_value=None, number_2_name=None, number_2_value=None), end_event=Event(subsystem=u'com.apple.Music', category=u'perf', name=u'quit', scope=u'Process', signpost_id=17216892719917625070L, process_name=u'Music', process_id=17083, thread_id=184473, emit_MCT_timestamp=269229791556816, timebase_ratio=1, metadata_string=u'', telemetry_enabled=False, is_animation=False, error=None, decomposed_metadata=[{u'Prefix': u''}], event_type=u'SignpostEvent_IntervalEnd', walltime=u'2019-05-20 14:17:51.128059-0700', overriding_begin_MCT_timestamp=None, overriding_end_MCT_timestamp=None, overriding_emit_MCT_timestamp=None, string_1_name=None, string_1_value=None, string_2_name=None, string_2_value=None, number_1_name=None, number_1_value=None, number_2_name=None, number_2_value=None), signpost_id=17216892719917625070L, string_1_name=None, string_1_value=None, string_2_name=None, string_2_value=None, number_1_name=None, number_1_value=None, number_2_name=None, number_2_value=None, overriding_begin_walltime=None, overriding_end_walltime=None)
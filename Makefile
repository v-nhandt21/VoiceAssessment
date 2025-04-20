check_asr:
	python whisper_wrapper.py 

launch_backend:
	python webApp.py 

test_client:
	python client.py 

launch_frontend:
	cd assessment_ui && make launch
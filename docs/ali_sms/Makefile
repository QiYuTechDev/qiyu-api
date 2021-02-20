run:
	poetry run uvicorn --reload ali_sms_api:app


download-dysms-api:export api-url=https://api.aliyun.com/api/product/describeApiWithDocList.json\?productName\=Dysmsapi\&productVersion\=2017-05-25
download-dysms-api:
	curl $(api-url) -o Dysmsapi.json


gen-code:code-dir=/Users/dabaichi/QiYuTechDev/code
gen-code:api-file=$(shell pwd)/Dysmsapi.json
gen-code:prefix=$(shell pwd)/prefix.txt
gen-code:output=$(shell pwd)/ali_sms_api/gen.py
gen-code:
	cd $(code-dir) && poetry run python code ali stub --prefix $(prefix) --output $(output) $(api-file)
	make format

test-load:code-dir=/Users/dabaichi/QiYuTechDev/code
test-load:api-file=$(shell pwd)/Dysmsapi.json
test-load:output=$(shell pwd)/gen.json
test-load:
	cd $(code-dir) && poetry run python code ali test --output $(output) $(api-file)

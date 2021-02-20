# 使用 pytest 运行测试生成代码
test-and-gen-type:
	poetry run pytest -s dtk_api


gen-code:code-dir=/Users/dabaichi/QiYuTechDev/code
gen-code:api-file=$(shell pwd)/api.json
gen-code:prefix=$(shell pwd)/prefix.txt
gen-code:output=$(shell pwd)/dtk_api/gen.py
gen-code:
	cd $(code-dir) && poetry run python code dtk stub --prefix $(prefix) --output $(output) $(api-file)
	make format

test-load:code-dir=/Users/dabaichi/QiYuTechDev/code
test-load:api-file=$(shell pwd)/api.json
test-load:output=$(shell pwd)/test.json
test-load:
	cd $(code-dir) && poetry run python code dtk test --output $(output) $(api-file)

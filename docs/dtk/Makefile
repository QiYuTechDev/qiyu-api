run:
	poetry run uvicorn --reload alisms:app

freeze:
	poetry export --without-hashes -f requirements.txt > requirements.txt

format:
	poetry run black dtk_api

outdated:http_proxy=http://127.0.0.1:8081
outdated:https_proxy=http://127.0.0.1:8081
outdated:
	poetry show -o

update:http_proxy=http://127.0.0.1:8081
update:https_proxy=http://127.0.0.1:8081
update:
	poetry update
	make freeze

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


publish:http_proxy=http://127.0.0.1:8081
publish:https_proxy=http://127.0.0.1:8081
publish:
	poetry publish --build

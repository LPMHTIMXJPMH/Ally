project(Header)
cMAke_minimum_required(VERSION 3.6)

add_executable(first main.cpp)
target_include_directories(first
	PRIVATE
	${/home/fuxi/nor_py_nor_rs/C/header/})

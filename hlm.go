/* -------------------------------------------------------------------
   | Hascal Programming Language --- Hascal Library Manager v0.2     |
   | Copyright (c) 2019-2021 Hascal Development Team                 |
   -------------------------------------------------------------------
*/
package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"runtime"
)

func main() {
	version := "0.2"
	if len(os.Args) < 2 {
		fmt.Println("hlm : no commands found\nusage : hlm install <lib_name>")
		os.Exit(0)
	}
	if os.Args[1] == "version" {
		fmt.Println("hlm : v",version,runtime.GOOS)
		os.Exit(0)
	}
	if os.Args[1] == "install" {
		fmt.Println("Installing from https://raw.githubusercontent.com/hascal/hlm-libs/main/libs/" + os.Args[2] + ".has to hlib/" + os.Args[2] + ".has")
		file, err := os.OpenFile("hlib/" + os.Args[2] + ".has", os.O_WRONLY | os.O_CREATE, 0755)
		if err != nil {
			panic(err)
		}
		defer file.Close()
		resp, err := http.Get("https://raw.githubusercontent.com/hascal/hlm-libs/main/libs/" + os.Args[2] + ".has")
		if err != nil {
			panic(err)
		}
		_, err = io.Copy(file, resp.Body)
		if err != nil {
			panic(err)
		}
		defer resp.Body.Close()
	}
}

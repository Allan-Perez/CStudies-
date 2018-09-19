(* int * int -> int * int *)
fun swap(tpl: int * bool)=
	(#2 tpl, #1 tpl)

(* (int*int) * (int*int) -> int*)
fun sumTpl (tpl1 : int * int, tpl2 : int * int)=
	(#1 tpl1) + (#2 tpl1) + (#1 tpl2) + (#2 tpl2)
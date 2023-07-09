	.file	"code.c"
	.text
	.section	.rodata
.LC0:
	.string	"%s"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movq	$0, -11(%rbp)
	movw	$0, -3(%rbp)
	movb	$0, -1(%rbp)
	movb	$65, -11(%rbp)
	movb	$115, -10(%rbp)
	movb	$77, -9(%rbp)
	movb	$95, -8(%rbp)
	movb	$64, -11(%rbp)
	movb	$49, -7(%rbp)
	movb	$115, -6(%rbp)
	movb	$51, -5(%rbp)
	movb	$69, -3(%rbp)
	movb	$122, -2(%rbp)
	movb	$95, -4(%rbp)
	movb	$42, -1(%rbp)
	leaq	-11(%rbp), %rax
	movq	%rax, %rsi
	movl	$.LC0, %edi
	movl	$0, %eax
	call	printf
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (GNU) 8.5.0 20210514 (Red Hat 8.5.0-18)"
	.section	.note.GNU-stack,"",@progbits

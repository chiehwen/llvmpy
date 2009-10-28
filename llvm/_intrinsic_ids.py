#
# Copyright (c) 2008, Mahadevan R All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
#  * Neither the name of this software, nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

"""Intrinsic IDs.

Intended to be imported into the llvm.core namespace. Not for public use."""


INTR_ALPHA_UMULH               = 1
INTR_ANNOTATION                = 2
INTR_ARM_NEON_VABALS           = 3
INTR_ARM_NEON_VABALU           = 4
INTR_ARM_NEON_VABAS            = 5
INTR_ARM_NEON_VABAU            = 6
INTR_ARM_NEON_VABDLS           = 7
INTR_ARM_NEON_VABDLU           = 8
INTR_ARM_NEON_VABDS            = 9
INTR_ARM_NEON_VABDU            = 10
INTR_ARM_NEON_VABS             = 11
INTR_ARM_NEON_VACGED           = 12
INTR_ARM_NEON_VACGEQ           = 13
INTR_ARM_NEON_VACGTD           = 14
INTR_ARM_NEON_VACGTQ           = 15
INTR_ARM_NEON_VADDHN           = 16
INTR_ARM_NEON_VADDLS           = 17
INTR_ARM_NEON_VADDLU           = 18
INTR_ARM_NEON_VADDWS           = 19
INTR_ARM_NEON_VADDWU           = 20
INTR_ARM_NEON_VCLS             = 21
INTR_ARM_NEON_VCLZ             = 22
INTR_ARM_NEON_VCNT             = 23
INTR_ARM_NEON_VCVTFP2FXS       = 24
INTR_ARM_NEON_VCVTFP2FXU       = 25
INTR_ARM_NEON_VCVTFXS2FP       = 26
INTR_ARM_NEON_VCVTFXU2FP       = 27
INTR_ARM_NEON_VHADDS           = 28
INTR_ARM_NEON_VHADDU           = 29
INTR_ARM_NEON_VHSUBS           = 30
INTR_ARM_NEON_VHSUBU           = 31
INTR_ARM_NEON_VLD1             = 32
INTR_ARM_NEON_VLD2             = 33
INTR_ARM_NEON_VLD2LANE         = 34
INTR_ARM_NEON_VLD3             = 35
INTR_ARM_NEON_VLD3LANE         = 36
INTR_ARM_NEON_VLD4             = 37
INTR_ARM_NEON_VLD4LANE         = 38
INTR_ARM_NEON_VMAXS            = 39
INTR_ARM_NEON_VMAXU            = 40
INTR_ARM_NEON_VMINS            = 41
INTR_ARM_NEON_VMINU            = 42
INTR_ARM_NEON_VMLALS           = 43
INTR_ARM_NEON_VMLALU           = 44
INTR_ARM_NEON_VMLSLS           = 45
INTR_ARM_NEON_VMLSLU           = 46
INTR_ARM_NEON_VMOVLS           = 47
INTR_ARM_NEON_VMOVLU           = 48
INTR_ARM_NEON_VMOVN            = 49
INTR_ARM_NEON_VMULLP           = 50
INTR_ARM_NEON_VMULLS           = 51
INTR_ARM_NEON_VMULLU           = 52
INTR_ARM_NEON_VMULP            = 53
INTR_ARM_NEON_VPADALS          = 54
INTR_ARM_NEON_VPADALU          = 55
INTR_ARM_NEON_VPADD            = 56
INTR_ARM_NEON_VPADDLS          = 57
INTR_ARM_NEON_VPADDLU          = 58
INTR_ARM_NEON_VPMAXS           = 59
INTR_ARM_NEON_VPMAXU           = 60
INTR_ARM_NEON_VPMINS           = 61
INTR_ARM_NEON_VPMINU           = 62
INTR_ARM_NEON_VQABS            = 63
INTR_ARM_NEON_VQADDS           = 64
INTR_ARM_NEON_VQADDU           = 65
INTR_ARM_NEON_VQDMLAL          = 66
INTR_ARM_NEON_VQDMLSL          = 67
INTR_ARM_NEON_VQDMULH          = 68
INTR_ARM_NEON_VQDMULL          = 69
INTR_ARM_NEON_VQMOVNS          = 70
INTR_ARM_NEON_VQMOVNSU         = 71
INTR_ARM_NEON_VQMOVNU          = 72
INTR_ARM_NEON_VQNEG            = 73
INTR_ARM_NEON_VQRDMULH         = 74
INTR_ARM_NEON_VQRSHIFTNS       = 75
INTR_ARM_NEON_VQRSHIFTNSU      = 76
INTR_ARM_NEON_VQRSHIFTNU       = 77
INTR_ARM_NEON_VQRSHIFTS        = 78
INTR_ARM_NEON_VQRSHIFTU        = 79
INTR_ARM_NEON_VQSHIFTNS        = 80
INTR_ARM_NEON_VQSHIFTNSU       = 81
INTR_ARM_NEON_VQSHIFTNU        = 82
INTR_ARM_NEON_VQSHIFTS         = 83
INTR_ARM_NEON_VQSHIFTSU        = 84
INTR_ARM_NEON_VQSHIFTU         = 85
INTR_ARM_NEON_VQSUBS           = 86
INTR_ARM_NEON_VQSUBU           = 87
INTR_ARM_NEON_VRADDHN          = 88
INTR_ARM_NEON_VRECPE           = 89
INTR_ARM_NEON_VRECPS           = 90
INTR_ARM_NEON_VRHADDS          = 91
INTR_ARM_NEON_VRHADDU          = 92
INTR_ARM_NEON_VRSHIFTN         = 93
INTR_ARM_NEON_VRSHIFTS         = 94
INTR_ARM_NEON_VRSHIFTU         = 95
INTR_ARM_NEON_VRSQRTE          = 96
INTR_ARM_NEON_VRSQRTS          = 97
INTR_ARM_NEON_VRSUBHN          = 98
INTR_ARM_NEON_VSHIFTINS        = 99
INTR_ARM_NEON_VSHIFTLS         = 100
INTR_ARM_NEON_VSHIFTLU         = 101
INTR_ARM_NEON_VSHIFTN          = 102
INTR_ARM_NEON_VSHIFTS          = 103
INTR_ARM_NEON_VSHIFTU          = 104
INTR_ARM_NEON_VST1             = 105
INTR_ARM_NEON_VST2             = 106
INTR_ARM_NEON_VST2LANE         = 107
INTR_ARM_NEON_VST3             = 108
INTR_ARM_NEON_VST3LANE         = 109
INTR_ARM_NEON_VST4             = 110
INTR_ARM_NEON_VST4LANE         = 111
INTR_ARM_NEON_VSUBHN           = 112
INTR_ARM_NEON_VSUBLS           = 113
INTR_ARM_NEON_VSUBLU           = 114
INTR_ARM_NEON_VSUBWS           = 115
INTR_ARM_NEON_VSUBWU           = 116
INTR_ARM_NEON_VTBL1            = 117
INTR_ARM_NEON_VTBL2            = 118
INTR_ARM_NEON_VTBL3            = 119
INTR_ARM_NEON_VTBL4            = 120
INTR_ARM_NEON_VTBX1            = 121
INTR_ARM_NEON_VTBX2            = 122
INTR_ARM_NEON_VTBX3            = 123
INTR_ARM_NEON_VTBX4            = 124
INTR_ARM_THREAD_POINTER        = 125
INTR_ATOMIC_CMP_SWAP           = 126
INTR_ATOMIC_LOAD_ADD           = 127
INTR_ATOMIC_LOAD_AND           = 128
INTR_ATOMIC_LOAD_MAX           = 129
INTR_ATOMIC_LOAD_MIN           = 130
INTR_ATOMIC_LOAD_NAND          = 131
INTR_ATOMIC_LOAD_OR            = 132
INTR_ATOMIC_LOAD_SUB           = 133
INTR_ATOMIC_LOAD_UMAX          = 134
INTR_ATOMIC_LOAD_UMIN          = 135
INTR_ATOMIC_LOAD_XOR           = 136
INTR_ATOMIC_SWAP               = 137
INTR_BFIN_CSYNC                = 138
INTR_BFIN_IDLE                 = 139
INTR_BFIN_SSYNC                = 140
INTR_BSWAP                     = 141
INTR_CONVERTFF                 = 142
INTR_CONVERTFSI                = 143
INTR_CONVERTFUI                = 144
INTR_CONVERTSIF                = 145
INTR_CONVERTSS                 = 146
INTR_CONVERTSU                 = 147
INTR_CONVERTUIF                = 148
INTR_CONVERTUS                 = 149
INTR_CONVERTUU                 = 150
INTR_COS                       = 151
INTR_CTLZ                      = 152
INTR_CTPOP                     = 153
INTR_CTTZ                      = 154
INTR_DBG_DECLARE               = 155
INTR_DBG_FUNC_START            = 156
INTR_DBG_REGION_END            = 157
INTR_DBG_REGION_START          = 158
INTR_DBG_STOPPOINT             = 159
INTR_EH_DWARF_CFA              = 160
INTR_EH_EXCEPTION              = 161
INTR_EH_RETURN_I32             = 162
INTR_EH_RETURN_I64             = 163
INTR_EH_SELECTOR_I32           = 164
INTR_EH_SELECTOR_I64           = 165
INTR_EH_SJLJ_LONGJMP           = 166
INTR_EH_SJLJ_LSDA              = 167
INTR_EH_SJLJ_SETJMP            = 168
INTR_EH_TYPEID_FOR_I32         = 169
INTR_EH_TYPEID_FOR_I64         = 170
INTR_EH_UNWIND_INIT            = 171
INTR_EXP                       = 172
INTR_EXP2                      = 173
INTR_FLT_ROUNDS                = 174
INTR_FRAMEADDRESS              = 175
INTR_GCREAD                    = 176
INTR_GCROOT                    = 177
INTR_GCWRITE                   = 178
INTR_INIT_TRAMPOLINE           = 179
INTR_LOG                       = 180
INTR_LOG10                     = 181
INTR_LOG2                      = 182
INTR_LONGJMP                   = 183
INTR_MEMCPY                    = 184
INTR_MEMMOVE                   = 185
INTR_MEMORY_BARRIER            = 186
INTR_MEMSET                    = 187
INTR_PCMARKER                  = 188
INTR_POW                       = 189
INTR_POWI                      = 190
INTR_PPC_ALTIVEC_DSS           = 191
INTR_PPC_ALTIVEC_DSSALL        = 192
INTR_PPC_ALTIVEC_DST           = 193
INTR_PPC_ALTIVEC_DSTST         = 194
INTR_PPC_ALTIVEC_DSTSTT        = 195
INTR_PPC_ALTIVEC_DSTT          = 196
INTR_PPC_ALTIVEC_LVEBX         = 197
INTR_PPC_ALTIVEC_LVEHX         = 198
INTR_PPC_ALTIVEC_LVEWX         = 199
INTR_PPC_ALTIVEC_LVSL          = 200
INTR_PPC_ALTIVEC_LVSR          = 201
INTR_PPC_ALTIVEC_LVX           = 202
INTR_PPC_ALTIVEC_LVXL          = 203
INTR_PPC_ALTIVEC_MFVSCR        = 204
INTR_PPC_ALTIVEC_MTVSCR        = 205
INTR_PPC_ALTIVEC_STVEBX        = 206
INTR_PPC_ALTIVEC_STVEHX        = 207
INTR_PPC_ALTIVEC_STVEWX        = 208
INTR_PPC_ALTIVEC_STVX          = 209
INTR_PPC_ALTIVEC_STVXL         = 210
INTR_PPC_ALTIVEC_VADDCUW       = 211
INTR_PPC_ALTIVEC_VADDSBS       = 212
INTR_PPC_ALTIVEC_VADDSHS       = 213
INTR_PPC_ALTIVEC_VADDSWS       = 214
INTR_PPC_ALTIVEC_VADDUBS       = 215
INTR_PPC_ALTIVEC_VADDUHS       = 216
INTR_PPC_ALTIVEC_VADDUWS       = 217
INTR_PPC_ALTIVEC_VAVGSB        = 218
INTR_PPC_ALTIVEC_VAVGSH        = 219
INTR_PPC_ALTIVEC_VAVGSW        = 220
INTR_PPC_ALTIVEC_VAVGUB        = 221
INTR_PPC_ALTIVEC_VAVGUH        = 222
INTR_PPC_ALTIVEC_VAVGUW        = 223
INTR_PPC_ALTIVEC_VCFSX         = 224
INTR_PPC_ALTIVEC_VCFUX         = 225
INTR_PPC_ALTIVEC_VCMPBFP       = 226
INTR_PPC_ALTIVEC_VCMPBFP_P     = 227
INTR_PPC_ALTIVEC_VCMPEQFP      = 228
INTR_PPC_ALTIVEC_VCMPEQFP_P    = 229
INTR_PPC_ALTIVEC_VCMPEQUB      = 230
INTR_PPC_ALTIVEC_VCMPEQUB_P    = 231
INTR_PPC_ALTIVEC_VCMPEQUH      = 232
INTR_PPC_ALTIVEC_VCMPEQUH_P    = 233
INTR_PPC_ALTIVEC_VCMPEQUW      = 234
INTR_PPC_ALTIVEC_VCMPEQUW_P    = 235
INTR_PPC_ALTIVEC_VCMPGEFP      = 236
INTR_PPC_ALTIVEC_VCMPGEFP_P    = 237
INTR_PPC_ALTIVEC_VCMPGTFP      = 238
INTR_PPC_ALTIVEC_VCMPGTFP_P    = 239
INTR_PPC_ALTIVEC_VCMPGTSB      = 240
INTR_PPC_ALTIVEC_VCMPGTSB_P    = 241
INTR_PPC_ALTIVEC_VCMPGTSH      = 242
INTR_PPC_ALTIVEC_VCMPGTSH_P    = 243
INTR_PPC_ALTIVEC_VCMPGTSW      = 244
INTR_PPC_ALTIVEC_VCMPGTSW_P    = 245
INTR_PPC_ALTIVEC_VCMPGTUB      = 246
INTR_PPC_ALTIVEC_VCMPGTUB_P    = 247
INTR_PPC_ALTIVEC_VCMPGTUH      = 248
INTR_PPC_ALTIVEC_VCMPGTUH_P    = 249
INTR_PPC_ALTIVEC_VCMPGTUW      = 250
INTR_PPC_ALTIVEC_VCMPGTUW_P    = 251
INTR_PPC_ALTIVEC_VCTSXS        = 252
INTR_PPC_ALTIVEC_VCTUXS        = 253
INTR_PPC_ALTIVEC_VEXPTEFP      = 254
INTR_PPC_ALTIVEC_VLOGEFP       = 255
INTR_PPC_ALTIVEC_VMADDFP       = 256
INTR_PPC_ALTIVEC_VMAXFP        = 257
INTR_PPC_ALTIVEC_VMAXSB        = 258
INTR_PPC_ALTIVEC_VMAXSH        = 259
INTR_PPC_ALTIVEC_VMAXSW        = 260
INTR_PPC_ALTIVEC_VMAXUB        = 261
INTR_PPC_ALTIVEC_VMAXUH        = 262
INTR_PPC_ALTIVEC_VMAXUW        = 263
INTR_PPC_ALTIVEC_VMHADDSHS     = 264
INTR_PPC_ALTIVEC_VMHRADDSHS    = 265
INTR_PPC_ALTIVEC_VMINFP        = 266
INTR_PPC_ALTIVEC_VMINSB        = 267
INTR_PPC_ALTIVEC_VMINSH        = 268
INTR_PPC_ALTIVEC_VMINSW        = 269
INTR_PPC_ALTIVEC_VMINUB        = 270
INTR_PPC_ALTIVEC_VMINUH        = 271
INTR_PPC_ALTIVEC_VMINUW        = 272
INTR_PPC_ALTIVEC_VMLADDUHM     = 273
INTR_PPC_ALTIVEC_VMSUMMBM      = 274
INTR_PPC_ALTIVEC_VMSUMSHM      = 275
INTR_PPC_ALTIVEC_VMSUMSHS      = 276
INTR_PPC_ALTIVEC_VMSUMUBM      = 277
INTR_PPC_ALTIVEC_VMSUMUHM      = 278
INTR_PPC_ALTIVEC_VMSUMUHS      = 279
INTR_PPC_ALTIVEC_VMULESB       = 280
INTR_PPC_ALTIVEC_VMULESH       = 281
INTR_PPC_ALTIVEC_VMULEUB       = 282
INTR_PPC_ALTIVEC_VMULEUH       = 283
INTR_PPC_ALTIVEC_VMULOSB       = 284
INTR_PPC_ALTIVEC_VMULOSH       = 285
INTR_PPC_ALTIVEC_VMULOUB       = 286
INTR_PPC_ALTIVEC_VMULOUH       = 287
INTR_PPC_ALTIVEC_VNMSUBFP      = 288
INTR_PPC_ALTIVEC_VPERM         = 289
INTR_PPC_ALTIVEC_VPKPX         = 290
INTR_PPC_ALTIVEC_VPKSHSS       = 291
INTR_PPC_ALTIVEC_VPKSHUS       = 292
INTR_PPC_ALTIVEC_VPKSWSS       = 293
INTR_PPC_ALTIVEC_VPKSWUS       = 294
INTR_PPC_ALTIVEC_VPKUHUS       = 295
INTR_PPC_ALTIVEC_VPKUWUS       = 296
INTR_PPC_ALTIVEC_VREFP         = 297
INTR_PPC_ALTIVEC_VRFIM         = 298
INTR_PPC_ALTIVEC_VRFIN         = 299
INTR_PPC_ALTIVEC_VRFIP         = 300
INTR_PPC_ALTIVEC_VRFIZ         = 301
INTR_PPC_ALTIVEC_VRLB          = 302
INTR_PPC_ALTIVEC_VRLH          = 303
INTR_PPC_ALTIVEC_VRLW          = 304
INTR_PPC_ALTIVEC_VRSQRTEFP     = 305
INTR_PPC_ALTIVEC_VSEL          = 306
INTR_PPC_ALTIVEC_VSL           = 307
INTR_PPC_ALTIVEC_VSLB          = 308
INTR_PPC_ALTIVEC_VSLH          = 309
INTR_PPC_ALTIVEC_VSLO          = 310
INTR_PPC_ALTIVEC_VSLW          = 311
INTR_PPC_ALTIVEC_VSR           = 312
INTR_PPC_ALTIVEC_VSRAB         = 313
INTR_PPC_ALTIVEC_VSRAH         = 314
INTR_PPC_ALTIVEC_VSRAW         = 315
INTR_PPC_ALTIVEC_VSRB          = 316
INTR_PPC_ALTIVEC_VSRH          = 317
INTR_PPC_ALTIVEC_VSRO          = 318
INTR_PPC_ALTIVEC_VSRW          = 319
INTR_PPC_ALTIVEC_VSUBCUW       = 320
INTR_PPC_ALTIVEC_VSUBSBS       = 321
INTR_PPC_ALTIVEC_VSUBSHS       = 322
INTR_PPC_ALTIVEC_VSUBSWS       = 323
INTR_PPC_ALTIVEC_VSUBUBS       = 324
INTR_PPC_ALTIVEC_VSUBUHS       = 325
INTR_PPC_ALTIVEC_VSUBUWS       = 326
INTR_PPC_ALTIVEC_VSUM2SWS      = 327
INTR_PPC_ALTIVEC_VSUM4SBS      = 328
INTR_PPC_ALTIVEC_VSUM4SHS      = 329
INTR_PPC_ALTIVEC_VSUM4UBS      = 330
INTR_PPC_ALTIVEC_VSUMSWS       = 331
INTR_PPC_ALTIVEC_VUPKHPX       = 332
INTR_PPC_ALTIVEC_VUPKHSB       = 333
INTR_PPC_ALTIVEC_VUPKHSH       = 334
INTR_PPC_ALTIVEC_VUPKLPX       = 335
INTR_PPC_ALTIVEC_VUPKLSB       = 336
INTR_PPC_ALTIVEC_VUPKLSH       = 337
INTR_PPC_DCBA                  = 338
INTR_PPC_DCBF                  = 339
INTR_PPC_DCBI                  = 340
INTR_PPC_DCBST                 = 341
INTR_PPC_DCBT                  = 342
INTR_PPC_DCBTST                = 343
INTR_PPC_DCBZ                  = 344
INTR_PPC_DCBZL                 = 345
INTR_PPC_SYNC                  = 346
INTR_PREFETCH                  = 347
INTR_PTR_ANNOTATION            = 348
INTR_READCYCLECOUNTER          = 349
INTR_RETURNADDRESS             = 350
INTR_SADD_WITH_OVERFLOW        = 351
INTR_SETJMP                    = 352
INTR_SIGLONGJMP                = 353
INTR_SIGSETJMP                 = 354
INTR_SIN                       = 355
INTR_SMUL_WITH_OVERFLOW        = 356
INTR_SPU_SI_A                  = 357
INTR_SPU_SI_ADDX               = 358
INTR_SPU_SI_AH                 = 359
INTR_SPU_SI_AHI                = 360
INTR_SPU_SI_AI                 = 361
INTR_SPU_SI_AND                = 362
INTR_SPU_SI_ANDBI              = 363
INTR_SPU_SI_ANDC               = 364
INTR_SPU_SI_ANDHI              = 365
INTR_SPU_SI_ANDI               = 366
INTR_SPU_SI_BG                 = 367
INTR_SPU_SI_BGX                = 368
INTR_SPU_SI_CEQ                = 369
INTR_SPU_SI_CEQB               = 370
INTR_SPU_SI_CEQBI              = 371
INTR_SPU_SI_CEQH               = 372
INTR_SPU_SI_CEQHI              = 373
INTR_SPU_SI_CEQI               = 374
INTR_SPU_SI_CG                 = 375
INTR_SPU_SI_CGT                = 376
INTR_SPU_SI_CGTB               = 377
INTR_SPU_SI_CGTBI              = 378
INTR_SPU_SI_CGTH               = 379
INTR_SPU_SI_CGTHI              = 380
INTR_SPU_SI_CGTI               = 381
INTR_SPU_SI_CGX                = 382
INTR_SPU_SI_CLGT               = 383
INTR_SPU_SI_CLGTB              = 384
INTR_SPU_SI_CLGTBI             = 385
INTR_SPU_SI_CLGTH              = 386
INTR_SPU_SI_CLGTHI             = 387
INTR_SPU_SI_CLGTI              = 388
INTR_SPU_SI_DFA                = 389
INTR_SPU_SI_DFM                = 390
INTR_SPU_SI_DFMA               = 391
INTR_SPU_SI_DFMS               = 392
INTR_SPU_SI_DFNMA              = 393
INTR_SPU_SI_DFNMS              = 394
INTR_SPU_SI_DFS                = 395
INTR_SPU_SI_FA                 = 396
INTR_SPU_SI_FCEQ               = 397
INTR_SPU_SI_FCGT               = 398
INTR_SPU_SI_FCMEQ              = 399
INTR_SPU_SI_FCMGT              = 400
INTR_SPU_SI_FM                 = 401
INTR_SPU_SI_FMA                = 402
INTR_SPU_SI_FMS                = 403
INTR_SPU_SI_FNMS               = 404
INTR_SPU_SI_FS                 = 405
INTR_SPU_SI_FSMBI              = 406
INTR_SPU_SI_MPY                = 407
INTR_SPU_SI_MPYA               = 408
INTR_SPU_SI_MPYH               = 409
INTR_SPU_SI_MPYHH              = 410
INTR_SPU_SI_MPYHHA             = 411
INTR_SPU_SI_MPYHHAU            = 412
INTR_SPU_SI_MPYHHU             = 413
INTR_SPU_SI_MPYI               = 414
INTR_SPU_SI_MPYS               = 415
INTR_SPU_SI_MPYU               = 416
INTR_SPU_SI_MPYUI              = 417
INTR_SPU_SI_NAND               = 418
INTR_SPU_SI_NOR                = 419
INTR_SPU_SI_OR                 = 420
INTR_SPU_SI_ORBI               = 421
INTR_SPU_SI_ORC                = 422
INTR_SPU_SI_ORHI               = 423
INTR_SPU_SI_ORI                = 424
INTR_SPU_SI_SF                 = 425
INTR_SPU_SI_SFH                = 426
INTR_SPU_SI_SFHI               = 427
INTR_SPU_SI_SFI                = 428
INTR_SPU_SI_SFX                = 429
INTR_SPU_SI_SHLI               = 430
INTR_SPU_SI_SHLQBI             = 431
INTR_SPU_SI_SHLQBII            = 432
INTR_SPU_SI_SHLQBY             = 433
INTR_SPU_SI_SHLQBYI            = 434
INTR_SPU_SI_XOR                = 435
INTR_SPU_SI_XORBI              = 436
INTR_SPU_SI_XORHI              = 437
INTR_SPU_SI_XORI               = 438
INTR_SQRT                      = 439
INTR_SSUB_WITH_OVERFLOW        = 440
INTR_STACKPROTECTOR            = 441
INTR_STACKRESTORE              = 442
INTR_STACKSAVE                 = 443
INTR_TRAP                      = 444
INTR_UADD_WITH_OVERFLOW        = 445
INTR_UMUL_WITH_OVERFLOW        = 446
INTR_USUB_WITH_OVERFLOW        = 447
INTR_VACOPY                    = 448
INTR_VAEND                     = 449
INTR_VAR_ANNOTATION            = 450
INTR_VASTART                   = 451
INTR_X86_MMX_EMMS              = 452
INTR_X86_MMX_FEMMS             = 453
INTR_X86_MMX_MASKMOVQ          = 454
INTR_X86_MMX_MOVNT_DQ          = 455
INTR_X86_MMX_PACKSSDW          = 456
INTR_X86_MMX_PACKSSWB          = 457
INTR_X86_MMX_PACKUSWB          = 458
INTR_X86_MMX_PADDS_B           = 459
INTR_X86_MMX_PADDS_W           = 460
INTR_X86_MMX_PADDUS_B          = 461
INTR_X86_MMX_PADDUS_W          = 462
INTR_X86_MMX_PAVG_B            = 463
INTR_X86_MMX_PAVG_W            = 464
INTR_X86_MMX_PCMPEQ_B          = 465
INTR_X86_MMX_PCMPEQ_D          = 466
INTR_X86_MMX_PCMPEQ_W          = 467
INTR_X86_MMX_PCMPGT_B          = 468
INTR_X86_MMX_PCMPGT_D          = 469
INTR_X86_MMX_PCMPGT_W          = 470
INTR_X86_MMX_PMADD_WD          = 471
INTR_X86_MMX_PMAXS_W           = 472
INTR_X86_MMX_PMAXU_B           = 473
INTR_X86_MMX_PMINS_W           = 474
INTR_X86_MMX_PMINU_B           = 475
INTR_X86_MMX_PMOVMSKB          = 476
INTR_X86_MMX_PMULH_W           = 477
INTR_X86_MMX_PMULHU_W          = 478
INTR_X86_MMX_PMULU_DQ          = 479
INTR_X86_MMX_PSAD_BW           = 480
INTR_X86_MMX_PSLL_D            = 481
INTR_X86_MMX_PSLL_Q            = 482
INTR_X86_MMX_PSLL_W            = 483
INTR_X86_MMX_PSLLI_D           = 484
INTR_X86_MMX_PSLLI_Q           = 485
INTR_X86_MMX_PSLLI_W           = 486
INTR_X86_MMX_PSRA_D            = 487
INTR_X86_MMX_PSRA_W            = 488
INTR_X86_MMX_PSRAI_D           = 489
INTR_X86_MMX_PSRAI_W           = 490
INTR_X86_MMX_PSRL_D            = 491
INTR_X86_MMX_PSRL_Q            = 492
INTR_X86_MMX_PSRL_W            = 493
INTR_X86_MMX_PSRLI_D           = 494
INTR_X86_MMX_PSRLI_Q           = 495
INTR_X86_MMX_PSRLI_W           = 496
INTR_X86_MMX_PSUBS_B           = 497
INTR_X86_MMX_PSUBS_W           = 498
INTR_X86_MMX_PSUBUS_B          = 499
INTR_X86_MMX_PSUBUS_W          = 500
INTR_X86_SSE2_ADD_SD           = 501
INTR_X86_SSE2_CLFLUSH          = 502
INTR_X86_SSE2_CMP_PD           = 503
INTR_X86_SSE2_CMP_SD           = 504
INTR_X86_SSE2_COMIEQ_SD        = 505
INTR_X86_SSE2_COMIGE_SD        = 506
INTR_X86_SSE2_COMIGT_SD        = 507
INTR_X86_SSE2_COMILE_SD        = 508
INTR_X86_SSE2_COMILT_SD        = 509
INTR_X86_SSE2_COMINEQ_SD       = 510
INTR_X86_SSE2_CVTDQ2PD         = 511
INTR_X86_SSE2_CVTDQ2PS         = 512
INTR_X86_SSE2_CVTPD2DQ         = 513
INTR_X86_SSE2_CVTPD2PS         = 514
INTR_X86_SSE2_CVTPS2DQ         = 515
INTR_X86_SSE2_CVTPS2PD         = 516
INTR_X86_SSE2_CVTSD2SI         = 517
INTR_X86_SSE2_CVTSD2SI64       = 518
INTR_X86_SSE2_CVTSD2SS         = 519
INTR_X86_SSE2_CVTSI2SD         = 520
INTR_X86_SSE2_CVTSI642SD       = 521
INTR_X86_SSE2_CVTSS2SD         = 522
INTR_X86_SSE2_CVTTPD2DQ        = 523
INTR_X86_SSE2_CVTTPS2DQ        = 524
INTR_X86_SSE2_CVTTSD2SI        = 525
INTR_X86_SSE2_CVTTSD2SI64      = 526
INTR_X86_SSE2_DIV_SD           = 527
INTR_X86_SSE2_LFENCE           = 528
INTR_X86_SSE2_LOADU_DQ         = 529
INTR_X86_SSE2_LOADU_PD         = 530
INTR_X86_SSE2_MASKMOV_DQU      = 531
INTR_X86_SSE2_MAX_PD           = 532
INTR_X86_SSE2_MAX_SD           = 533
INTR_X86_SSE2_MFENCE           = 534
INTR_X86_SSE2_MIN_PD           = 535
INTR_X86_SSE2_MIN_SD           = 536
INTR_X86_SSE2_MOVMSK_PD        = 537
INTR_X86_SSE2_MOVNT_DQ         = 538
INTR_X86_SSE2_MOVNT_I          = 539
INTR_X86_SSE2_MOVNT_PD         = 540
INTR_X86_SSE2_MUL_SD           = 541
INTR_X86_SSE2_PACKSSDW_128     = 542
INTR_X86_SSE2_PACKSSWB_128     = 543
INTR_X86_SSE2_PACKUSWB_128     = 544
INTR_X86_SSE2_PADDS_B          = 545
INTR_X86_SSE2_PADDS_W          = 546
INTR_X86_SSE2_PADDUS_B         = 547
INTR_X86_SSE2_PADDUS_W         = 548
INTR_X86_SSE2_PAVG_B           = 549
INTR_X86_SSE2_PAVG_W           = 550
INTR_X86_SSE2_PCMPEQ_B         = 551
INTR_X86_SSE2_PCMPEQ_D         = 552
INTR_X86_SSE2_PCMPEQ_W         = 553
INTR_X86_SSE2_PCMPGT_B         = 554
INTR_X86_SSE2_PCMPGT_D         = 555
INTR_X86_SSE2_PCMPGT_W         = 556
INTR_X86_SSE2_PMADD_WD         = 557
INTR_X86_SSE2_PMAXS_W          = 558
INTR_X86_SSE2_PMAXU_B          = 559
INTR_X86_SSE2_PMINS_W          = 560
INTR_X86_SSE2_PMINU_B          = 561
INTR_X86_SSE2_PMOVMSKB_128     = 562
INTR_X86_SSE2_PMULH_W          = 563
INTR_X86_SSE2_PMULHU_W         = 564
INTR_X86_SSE2_PMULU_DQ         = 565
INTR_X86_SSE2_PSAD_BW          = 566
INTR_X86_SSE2_PSLL_D           = 567
INTR_X86_SSE2_PSLL_DQ          = 568
INTR_X86_SSE2_PSLL_DQ_BS       = 569
INTR_X86_SSE2_PSLL_Q           = 570
INTR_X86_SSE2_PSLL_W           = 571
INTR_X86_SSE2_PSLLI_D          = 572
INTR_X86_SSE2_PSLLI_Q          = 573
INTR_X86_SSE2_PSLLI_W          = 574
INTR_X86_SSE2_PSRA_D           = 575
INTR_X86_SSE2_PSRA_W           = 576
INTR_X86_SSE2_PSRAI_D          = 577
INTR_X86_SSE2_PSRAI_W          = 578
INTR_X86_SSE2_PSRL_D           = 579
INTR_X86_SSE2_PSRL_DQ          = 580
INTR_X86_SSE2_PSRL_DQ_BS       = 581
INTR_X86_SSE2_PSRL_Q           = 582
INTR_X86_SSE2_PSRL_W           = 583
INTR_X86_SSE2_PSRLI_D          = 584
INTR_X86_SSE2_PSRLI_Q          = 585
INTR_X86_SSE2_PSRLI_W          = 586
INTR_X86_SSE2_PSUBS_B          = 587
INTR_X86_SSE2_PSUBS_W          = 588
INTR_X86_SSE2_PSUBUS_B         = 589
INTR_X86_SSE2_PSUBUS_W         = 590
INTR_X86_SSE2_SQRT_PD          = 591
INTR_X86_SSE2_SQRT_SD          = 592
INTR_X86_SSE2_STOREL_DQ        = 593
INTR_X86_SSE2_STOREU_DQ        = 594
INTR_X86_SSE2_STOREU_PD        = 595
INTR_X86_SSE2_SUB_SD           = 596
INTR_X86_SSE2_UCOMIEQ_SD       = 597
INTR_X86_SSE2_UCOMIGE_SD       = 598
INTR_X86_SSE2_UCOMIGT_SD       = 599
INTR_X86_SSE2_UCOMILE_SD       = 600
INTR_X86_SSE2_UCOMILT_SD       = 601
INTR_X86_SSE2_UCOMINEQ_SD      = 602
INTR_X86_SSE3_ADDSUB_PD        = 603
INTR_X86_SSE3_ADDSUB_PS        = 604
INTR_X86_SSE3_HADD_PD          = 605
INTR_X86_SSE3_HADD_PS          = 606
INTR_X86_SSE3_HSUB_PD          = 607
INTR_X86_SSE3_HSUB_PS          = 608
INTR_X86_SSE3_LDU_DQ           = 609
INTR_X86_SSE3_MONITOR          = 610
INTR_X86_SSE3_MWAIT            = 611
INTR_X86_SSE41_BLENDPD         = 612
INTR_X86_SSE41_BLENDPS         = 613
INTR_X86_SSE41_BLENDVPD        = 614
INTR_X86_SSE41_BLENDVPS        = 615
INTR_X86_SSE41_DPPD            = 616
INTR_X86_SSE41_DPPS            = 617
INTR_X86_SSE41_EXTRACTPS       = 618
INTR_X86_SSE41_INSERTPS        = 619
INTR_X86_SSE41_MOVNTDQA        = 620
INTR_X86_SSE41_MPSADBW         = 621
INTR_X86_SSE41_PACKUSDW        = 622
INTR_X86_SSE41_PBLENDVB        = 623
INTR_X86_SSE41_PBLENDW         = 624
INTR_X86_SSE41_PCMPEQQ         = 625
INTR_X86_SSE41_PEXTRB          = 626
INTR_X86_SSE41_PEXTRD          = 627
INTR_X86_SSE41_PEXTRQ          = 628
INTR_X86_SSE41_PHMINPOSUW      = 629
INTR_X86_SSE41_PMAXSB          = 630
INTR_X86_SSE41_PMAXSD          = 631
INTR_X86_SSE41_PMAXUD          = 632
INTR_X86_SSE41_PMAXUW          = 633
INTR_X86_SSE41_PMINSB          = 634
INTR_X86_SSE41_PMINSD          = 635
INTR_X86_SSE41_PMINUD          = 636
INTR_X86_SSE41_PMINUW          = 637
INTR_X86_SSE41_PMOVSXBD        = 638
INTR_X86_SSE41_PMOVSXBQ        = 639
INTR_X86_SSE41_PMOVSXBW        = 640
INTR_X86_SSE41_PMOVSXDQ        = 641
INTR_X86_SSE41_PMOVSXWD        = 642
INTR_X86_SSE41_PMOVSXWQ        = 643
INTR_X86_SSE41_PMOVZXBD        = 644
INTR_X86_SSE41_PMOVZXBQ        = 645
INTR_X86_SSE41_PMOVZXBW        = 646
INTR_X86_SSE41_PMOVZXDQ        = 647
INTR_X86_SSE41_PMOVZXWD        = 648
INTR_X86_SSE41_PMOVZXWQ        = 649
INTR_X86_SSE41_PMULDQ          = 650
INTR_X86_SSE41_PMULLD          = 651
INTR_X86_SSE41_PTESTC          = 652
INTR_X86_SSE41_PTESTNZC        = 653
INTR_X86_SSE41_PTESTZ          = 654
INTR_X86_SSE41_ROUND_PD        = 655
INTR_X86_SSE41_ROUND_PS        = 656
INTR_X86_SSE41_ROUND_SD        = 657
INTR_X86_SSE41_ROUND_SS        = 658
INTR_X86_SSE42_CRC32_16        = 659
INTR_X86_SSE42_CRC32_32        = 660
INTR_X86_SSE42_CRC32_64        = 661
INTR_X86_SSE42_CRC32_8         = 662
INTR_X86_SSE42_PCMPESTRI128    = 663
INTR_X86_SSE42_PCMPESTRIA128   = 664
INTR_X86_SSE42_PCMPESTRIC128   = 665
INTR_X86_SSE42_PCMPESTRIO128   = 666
INTR_X86_SSE42_PCMPESTRIS128   = 667
INTR_X86_SSE42_PCMPESTRIZ128   = 668
INTR_X86_SSE42_PCMPESTRM128    = 669
INTR_X86_SSE42_PCMPGTQ         = 670
INTR_X86_SSE42_PCMPISTRI128    = 671
INTR_X86_SSE42_PCMPISTRIA128   = 672
INTR_X86_SSE42_PCMPISTRIC128   = 673
INTR_X86_SSE42_PCMPISTRIO128   = 674
INTR_X86_SSE42_PCMPISTRIS128   = 675
INTR_X86_SSE42_PCMPISTRIZ128   = 676
INTR_X86_SSE42_PCMPISTRM128    = 677
INTR_X86_SSE_ADD_SS            = 678
INTR_X86_SSE_CMP_PS            = 679
INTR_X86_SSE_CMP_SS            = 680
INTR_X86_SSE_COMIEQ_SS         = 681
INTR_X86_SSE_COMIGE_SS         = 682
INTR_X86_SSE_COMIGT_SS         = 683
INTR_X86_SSE_COMILE_SS         = 684
INTR_X86_SSE_COMILT_SS         = 685
INTR_X86_SSE_COMINEQ_SS        = 686
INTR_X86_SSE_CVTPD2PI          = 687
INTR_X86_SSE_CVTPI2PD          = 688
INTR_X86_SSE_CVTPI2PS          = 689
INTR_X86_SSE_CVTPS2PI          = 690
INTR_X86_SSE_CVTSI2SS          = 691
INTR_X86_SSE_CVTSI642SS        = 692
INTR_X86_SSE_CVTSS2SI          = 693
INTR_X86_SSE_CVTSS2SI64        = 694
INTR_X86_SSE_CVTTPD2PI         = 695
INTR_X86_SSE_CVTTPS2PI         = 696
INTR_X86_SSE_CVTTSS2SI         = 697
INTR_X86_SSE_CVTTSS2SI64       = 698
INTR_X86_SSE_DIV_SS            = 699
INTR_X86_SSE_LDMXCSR           = 700
INTR_X86_SSE_LOADU_PS          = 701
INTR_X86_SSE_MAX_PS            = 702
INTR_X86_SSE_MAX_SS            = 703
INTR_X86_SSE_MIN_PS            = 704
INTR_X86_SSE_MIN_SS            = 705
INTR_X86_SSE_MOVMSK_PS         = 706
INTR_X86_SSE_MOVNT_PS          = 707
INTR_X86_SSE_MUL_SS            = 708
INTR_X86_SSE_RCP_PS            = 709
INTR_X86_SSE_RCP_SS            = 710
INTR_X86_SSE_RSQRT_PS          = 711
INTR_X86_SSE_RSQRT_SS          = 712
INTR_X86_SSE_SFENCE            = 713
INTR_X86_SSE_SQRT_PS           = 714
INTR_X86_SSE_SQRT_SS           = 715
INTR_X86_SSE_STMXCSR           = 716
INTR_X86_SSE_STOREU_PS         = 717
INTR_X86_SSE_SUB_SS            = 718
INTR_X86_SSE_UCOMIEQ_SS        = 719
INTR_X86_SSE_UCOMIGE_SS        = 720
INTR_X86_SSE_UCOMIGT_SS        = 721
INTR_X86_SSE_UCOMILE_SS        = 722
INTR_X86_SSE_UCOMILT_SS        = 723
INTR_X86_SSE_UCOMINEQ_SS       = 724
INTR_X86_SSSE3_PABS_B          = 725
INTR_X86_SSSE3_PABS_B_128      = 726
INTR_X86_SSSE3_PABS_D          = 727
INTR_X86_SSSE3_PABS_D_128      = 728
INTR_X86_SSSE3_PABS_W          = 729
INTR_X86_SSSE3_PABS_W_128      = 730
INTR_X86_SSSE3_PALIGN_R        = 731
INTR_X86_SSSE3_PALIGN_R_128    = 732
INTR_X86_SSSE3_PHADD_D         = 733
INTR_X86_SSSE3_PHADD_D_128     = 734
INTR_X86_SSSE3_PHADD_SW        = 735
INTR_X86_SSSE3_PHADD_SW_128    = 736
INTR_X86_SSSE3_PHADD_W         = 737
INTR_X86_SSSE3_PHADD_W_128     = 738
INTR_X86_SSSE3_PHSUB_D         = 739
INTR_X86_SSSE3_PHSUB_D_128     = 740
INTR_X86_SSSE3_PHSUB_SW        = 741
INTR_X86_SSSE3_PHSUB_SW_128    = 742
INTR_X86_SSSE3_PHSUB_W         = 743
INTR_X86_SSSE3_PHSUB_W_128     = 744
INTR_X86_SSSE3_PMADD_UB_SW     = 745
INTR_X86_SSSE3_PMADD_UB_SW_128 = 746
INTR_X86_SSSE3_PMUL_HR_SW      = 747
INTR_X86_SSSE3_PMUL_HR_SW_128  = 748
INTR_X86_SSSE3_PSHUF_B         = 749
INTR_X86_SSSE3_PSHUF_B_128     = 750
INTR_X86_SSSE3_PSIGN_B         = 751
INTR_X86_SSSE3_PSIGN_B_128     = 752
INTR_X86_SSSE3_PSIGN_D         = 753
INTR_X86_SSSE3_PSIGN_D_128     = 754
INTR_X86_SSSE3_PSIGN_W         = 755
INTR_X86_SSSE3_PSIGN_W_128     = 756
INTR_XCORE_BITREV              = 757
INTR_XCORE_GETID               = 758
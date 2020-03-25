/* This file was generated by lv6 version 6.101.17. */
/*  lv6 -n Main -2c -cc robustSpec_v2.lus */
/* on s27 the 24/03/2020 at 22:25:57 */

#ifndef _SOC2C_PREDEF_TYPES
#define _SOC2C_PREDEF_TYPES
typedef int _boolean;
typedef int _integer;
typedef char* _string;
typedef double _real;
typedef double _double;
typedef float _float;
#define _false 0
#define _true 1
#endif
// end of _SOC2C_PREDEF_TYPES
// User typedef 
#ifndef _robustSpec_v2_Main_TYPES
#define _robustSpec_v2_Main_TYPES
#endif // enf of  _robustSpec_v2_Main_TYPES
// Memoryless soc ctx typedef 
// Memoryfull soc ctx typedef 
/* Lustre_pre_ctx */
typedef struct {
   /*Memory cell*/
   _real _memory ;
} Lustre_pre_ctx_type;

/* Lustre_arrow_ctx */
typedef struct {
   /*Memory cell*/
   _boolean _memory ;
} Lustre_arrow_ctx_type;

/* robustSpec_v2_Max_ctx */
typedef struct {
   /*INSTANCES*/
   Lustre_pre_ctx_type Lustre_pre_ctx_tab[2];
   Lustre_arrow_ctx_type Lustre_arrow_ctx_tab[1];
} robustSpec_v2_Max_ctx_type;

/* robustSpec_v2_Once_Inf_ctx */
typedef struct {
   /*INSTANCES*/
   robustSpec_v2_Max_ctx_type robustSpec_v2_Max_ctx_tab[1];
} robustSpec_v2_Once_Inf_ctx_type;

/* robustSpec_v2_Main_ctx */
typedef struct {
   /*INSTANCES*/
   robustSpec_v2_Once_Inf_ctx_type robustSpec_v2_Once_Inf_ctx_tab[1];
} robustSpec_v2_Main_ctx_type;

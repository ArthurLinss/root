// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME G__AnalysisLib
#define R__NO_DEPRECATION

/*******************************************************************/
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define G__DICTIONARY
#include "RConfig.h"
#include "TClass.h"
#include "TDictAttributeMap.h"
#include "TInterpreter.h"
#include "TROOT.h"
#include "TBuffer.h"
#include "TMemberInspector.h"
#include "TInterpreter.h"
#include "TVirtualMutex.h"
#include "TError.h"

#ifndef G__ROOT
#define G__ROOT
#endif

#include "RtypesImp.h"
#include "TIsAProxy.h"
#include "TFileMergeInfo.h"
#include <algorithm>
#include "TCollectionProxyInfo.h"
/*******************************************************************/

#include "TDataMember.h"

// The generated code does not explicitly qualifies STL entities
namespace std {} using namespace std;

// Header files passed as explicit arguments
#include "../header/head.h"

// Header files passed via #pragma extra_include

namespace {
  void TriggerDictionaryInitialization_libAnalysisLib_Impl() {
    static const char* headers[] = {
"../header/head.h",
0
    };
    static const char* includePaths[] = {
"/cvmfs/sft.cern.ch/lcg/views/LCG_97a/x86_64-centos7-gcc8-opt/include",
"/afs/desy.de/user/a/arli/tutoria/pyroot_dic/header",
"/afs/desy.de/user/a/arli/tutoria/pyroot_dic",
"/cvmfs/sft.cern.ch/lcg/releases/ROOT/v6.20.06-3f7fd/x86_64-centos7-gcc8-opt/include/",
"/afs/desy.de/user/a/arli/tutoria/pyroot_dic/build/",
0
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "libAnalysisLib dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_Autoloading_Map;
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "libAnalysisLib dictionary payload"


#define _BACKWARD_BACKWARD_WARNING_H
// Inline headers
#include "../header/head.h"

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[] = {
nullptr
};
    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("libAnalysisLib",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_libAnalysisLib_Impl, {}, classesHeaders, /*hasCxxModule*/false);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_libAnalysisLib_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_libAnalysisLib() {
  TriggerDictionaryInitialization_libAnalysisLib_Impl();
}

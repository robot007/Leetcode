#include "stdafx.h"
#include "CppUnitTest.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest
{		
	TEST_CLASS(UnitTest1)
	{
	public:
		// int test();

		TEST_METHOD(Test1)
		{
			// TODO: Your test code here
			Assert::AreEqual(1, 1);
			
		}

		TEST_METHOD(Test2)
		{
			Assert(test() );
		}

		int test(void )
		{
			return 1;
		}
	};


}
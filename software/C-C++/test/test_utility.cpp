#include <gtest/gtest.h>
#include "my_library/my_utility.h"

// Test fixture for utility functions
class UtilityTest : public ::testing::Test {
protected:
    // SetUp method to initialize common resources for tests
    void SetUp() override {
        // Add setup code here if needed
    }

    // TearDown method to release resources after tests
    void TearDown() override {
        // Add teardown code here if needed
    }
};

// Test case for utilityFunction1
TEST_F(UtilityTest, TestUtilityFunction1) {
    // Test the utilityFunction1
    ASSERT_EQ(utilityFunction1(), 42);
}

// Test case for utilityFunction2
TEST_F(UtilityTest, TestUtilityFunction2) {
    // Test the utilityFunction2
    ASSERT_EQ(utilityFunction2(5), 10);
}

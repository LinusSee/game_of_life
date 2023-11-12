module RulesTest exposing (..)

import Expect
import Test exposing (..)


rulesSuite : Test
rulesSuite =
    describe "Testing GameOfLifeRules"
        [ test "example" <|
            \_ ->
                Expect.equal "hello" "hello"
        ]

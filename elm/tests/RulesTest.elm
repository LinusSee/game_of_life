module RulesTest exposing (..)

import Expect
import Rule
import Test exposing (..)


rulesSuite : Test
rulesSuite =
    describe "Testing GameOfLifeRules"
        [ describe "underpopulation"
            [ test "cell should die with 0 neighbours" <|
                \_ ->
                    let
                        isAlive =
                            Rule.cellWillBeAlive True 0
                    in
                    Expect.equal False isAlive
            , test "cell should die with 1 neighbour" <|
                \_ ->
                    let
                        isAlive =
                            Rule.cellWillBeAlive True 1
                    in
                    Expect.equal False isAlive
            , test "cell should remain dead with 0 neighbours" <|
                \_ ->
                    let
                        isAlive =
                            Rule.cellWillBeAlive False 0
                    in
                    Expect.equal False isAlive
            , test "cell should remain dead with 1 neighbours" <|
                \_ ->
                    let
                        isAlive =
                            Rule.cellWillBeAlive False 1
                    in
                    Expect.equal False isAlive
            ]
        , describe "survival"
            [ test "cell should survive with 2 neighbours" <|
                \_ ->
                    let
                        isAlive =
                            Rule.cellWillBeAlive True 2
                    in
                    Expect.equal True isAlive
            , test "cell should survive with 3 neighbours" <|
                \_ ->
                    let
                        isAlive =
                            Rule.cellWillBeAlive True 3
                    in
                    Expect.equal True isAlive
            , test "cell should remain dead with 2 neighbours" <|
                \_ ->
                    let
                        isAlive =
                            Rule.cellWillBeAlive False 2
                    in
                    Expect.equal False isAlive
            ]
        , describe "overpopulation"
            [ test "cell should die with more than 3 neighbours" <|
                \_ ->
                    let
                        scenarios =
                            [ { isAlive = True, neighbours = 4 } ]

                        checkIsAlive =
                            \{ isAlive, neighbours } -> Rule.cellWillBeAlive isAlive neighbours
                    in
                    False
                        |> Expect.all
                            (scenarios
                                |> List.map checkIsAlive
                                |> List.map Expect.equal
                            )
            , test "cell should remain dead with more than 3 neighbours" <|
                \_ ->
                    let
                        scenarios =
                            [ { isAlive = False, neighbours = 4 } ]

                        checkIsAlive =
                            \{ isAlive, neighbours } -> Rule.cellWillBeAlive isAlive neighbours
                    in
                    False
                        |> Expect.all
                            (scenarios
                                |> List.map checkIsAlive
                                |> List.map Expect.equal
                            )
            ]
        , describe "revival"
            [ test "cell should come alive with 3 neighbours" <|
                \_ ->
                    let
                        isAlive =
                            Rule.cellWillBeAlive False 3
                    in
                    Expect.equal True isAlive
            ]
        ]

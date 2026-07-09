from maintainability_index import get_maintainability_rating


def generate_report(
    functions,
    classes,
    imports,
    total_lines,
    blank_lines,
    comment_lines,
    code_lines,
    largest_function,
    smallest_function,
    average_function_size,
    long_functions,
    complexity,
    rating,
    duplicate_functions,
    todo,
    fixme,
    bug,
    dependencies,
    unused_imports,
    unused_variables,
    bad_function_names,
    detected_long_functions,
    missing_docstrings,
    many_argument_functions,
    nested_depth,
    empty_exception_handlers,
    global_variables,
    magic_numbers,
    function_calls,
    recursive_functions,
    dead_code,
    classes_without_init,
    many_method_classes,
    inheritance,
    lambda_functions,
    try_without_finally,
    hardcoded_passwords,
    large_classes,
    import_aliases,
    function_complexity,
    file_metrics,
    maintainability_score,
    security_report,
    health_report,
    requirements_list
):

    print("\n" + "=" * 60)
    print("        CODE ANALYSIS REPORT")
    print("=" * 60)


    print(f"\nFunctions : {len(functions)}")
    print(f"Classes   : {len(classes)}")
    print(f"Imports   : {len(imports)}")


    print("\nProject Metrics")
    print("-" * 40)

    print(f"Total Lines   : {total_lines}")
    print(f"Code Lines    : {code_lines}")
    print(f"Blank Lines   : {blank_lines}")
    print(f"Comment Lines : {comment_lines}")



    print("\nFunction Metrics")
    print("-" * 40)

    print(f"Largest Function : {largest_function}")
    print(f"Smallest Function : {smallest_function}")
    print(f"Average Function Size : {average_function_size:.2f}")



    print("\nComplexity")
    print("-" * 40)

    print(f"Complexity Score : {complexity}")
    print(f"Quality Rating   : {rating}")



    print("\nDuplicate Functions")
    print("-" * 40)

    if duplicate_functions:

        for function in duplicate_functions:
            print(f"• {function}")

    else:

        print("No duplicate functions found.")




    print("\nTask Comments")
    print("-" * 40)

    print(f"TODO  : {todo}")
    print(f"FIXME : {fixme}")
    print(f"BUG   : {bug}")




    print("\nDependencies")
    print("-" * 40)

    if dependencies:

        for dependency in dependencies:
            print(f"• {dependency}")

    else:

        print("No dependencies found.")




    print("\nUnused Imports")
    print("-" * 40)

    if unused_imports:

        for module in unused_imports:
            print(f"• {module}")

    else:

        print("No unused imports found.")




    print("\nUnused Variables")
    print("-" * 40)

    if unused_variables:

        for variable in unused_variables:
            print(f"• {variable}")

    else:

        print("No unused variables found.")




    print("\nNaming Convention Warnings")
    print("-" * 40)

    if bad_function_names:

        for name in bad_function_names:
            print(f"• {name}")

    else:

        print("All function names follow snake_case.")




    print("\nLong Functions")
    print("-" * 40)

    if detected_long_functions:

        for name, size in detected_long_functions:
            print(f"• {name} ({size} lines)")

    else:

        print("No long functions found.")




    print("\nFunctions Missing Docstrings")
    print("-" * 40)

    if missing_docstrings:

        for function in missing_docstrings:
            print(f"• {function}")

    else:

        print("Every function has a docstring.")




    print("\nFunctions With Too Many Arguments")
    print("-" * 40)

    if many_argument_functions:

        for name, count in many_argument_functions:
            print(f"• {name} ({count} arguments)")

    else:

        print("No functions exceed the argument limit.")




    print("\nNested Loop Analysis")
    print("-" * 40)

    print(f"Maximum Loop Depth : {nested_depth}")

    if nested_depth >= 3:

        print("Warning : Deeply Nested Loops Found")

    else:

        print("Loop nesting is acceptable.")




    print("\nEmpty Exception Handlers")
    print("-" * 40)

    if empty_exception_handlers:

        for line in empty_exception_handlers:
            print(f"• Line {line}")

    else:

        print("No empty exception handlers found.")




    print("\nGlobal Variables")
    print("-" * 40)

    if global_variables:

        for variable in global_variables:
            print(f"• {variable}")

    else:

        print("No global variables found.")




    print("\nMagic Numbers")
    print("-" * 40)

    if magic_numbers:

        for number in magic_numbers:
            print(f"• {number}")

    else:

        print("No magic numbers found.")




    print("\nFunction Call Counts")
    print("-" * 40)

    if function_calls:

        for function, count in function_calls.items():

            print(f"• {function} : {count}")

    else:

        print("No function calls found.")




    print("\nRecursive Functions")
    print("-" * 40)

    if recursive_functions:

        for function in recursive_functions:

            print(f"• {function}")

    else:

        print("No recursive functions found.")




    # Lesson 63
    print("\nDead Code Detection")
    print("-" * 40)

    if dead_code:

        for function in dead_code:

            print(f"• {function}")

    else:

        print("No dead code detected.")




    # Lesson 64
    print("\nClasses Without __init__()")
    print("-" * 40)

    if classes_without_init:

        for cls in classes_without_init:

            print(f"• {cls}")

    else:

        print("All classes have __init__() method.")

    print("\nClasses With Too Many Methods")
    print("-" * 40)

    if many_method_classes:

        for name, count in many_method_classes:

            print(f"• {name} ({count} methods)")

    else:

        print("No large classes found.")

    print("\nInheritance Relationships")
    print("-" * 40)

    if inheritance:

        for child, parent in inheritance:

         print(f"• {child} → {parent}")

    else:

        print("No inheritance detected.")


    print("\nLambda Functions")
    print("-" * 40)

    if lambda_functions:

        for line in lambda_functions:

            print(f"• Line {line}")

    else:

        print("No lambda functions found.")


    print("\nTry Blocks Without Finally")
    print("-" * 40)

    if try_without_finally:

        for line in try_without_finally:

            print(f"• Line {line}")
    else:

        print("All try blocks contain finally.")

    print("\nHardcoded Passwords")
    print("-" * 40)

    if hardcoded_passwords:

        for variable, line in hardcoded_passwords:

            print(f"• {variable} (Line {line})")

    else:

        print("No hardcoded passwords found.")

    print("\nLarge Classes")
    print("-" * 40)

    if large_classes:

        for name, methods in large_classes:

            print(f"• {name} ({methods} methods)")

    else:

        print("No large classes found.")

    print("\nImport Aliases")
    print("-" * 40)

    if import_aliases:

        for module, alias in import_aliases:

            print(f"• {module} → {alias}")

    else:

        print("No import aliases found.")


    # Lesson 70
    print("\nFunction Complexity Report")
    print("-" * 40)

    if function_complexity:

        for entry in function_complexity:
            print(
                f"• {entry['name']} ({entry['file']}, line {entry['line']}) "
                f"- Complexity {entry['complexity']} - {entry['rating']}"
            )

    else:

        print("No functions found to analyze.")


    # Lesson 71
    print("\nFile-wise Metrics")
    print("-" * 40)

    if file_metrics:

        for f in file_metrics:
            print(
                f"• {f['file']} — Lines: {f['total_lines']}, "
                f"Code: {f['code_lines']}, Functions: {f['function_count']}, "
                f"Classes: {f['class_count']}, Complexity: {f['total_complexity']}"
            )

    else:

        print("No file metrics available.")


    # Lesson 72
    print("\nMaintainability Index")
    print("-" * 40)

    print(f"Average Maintainability Score : {maintainability_score}")
    print(f"Rating                        : {get_maintainability_rating(maintainability_score)}")


    # Lesson 73
    print("\nSecurity Score")
    print("-" * 40)

    print(f"Score  : {security_report['score']} / 100")
    print(f"Rating : {security_report['rating']}")

    for issue, count in security_report["issues_found"].items():
        print(f"• {issue.replace('_', ' ').title()} : {count}")


    # Lesson 74
    print("\nOverall Code Health Score")
    print("-" * 40)

    print(f"Overall Score : {health_report['overall_score']} / 100")
    print(f"Grade         : {health_report['grade']}")

    for metric, score in health_report["breakdown"].items():
        print(f"• {metric.replace('_', ' ').title()} : {score}")


    # Lesson 76
    print("\nDetected Third-Party Requirements")
    print("-" * 40)

    if requirements_list:

        for package in requirements_list:
            print(f"• {package}")

    else:

        print("No third-party packages detected.")


    print("\n" + "=" * 60)
    print("        END OF REPORT")
    print("=" * 60)

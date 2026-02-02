
## Summary table

# | Pattern    | Meaning                                |
# | ---------- | -------------------------------------- |
# | `_name`    | Internal / protected by convention     |
# | `__name`   | Name-mangled (avoid subclass conflict) |
# | `__name__` | Python special (magic) method          |
# | `name_`    | Avoid keyword clash                    |
# | `_`        | Throwaway / last result                |


## Rule of thumb

# * **Do not access `_name`** unless necessary
# * **Do not invent new `__name__` methods**
# * Use `__name` only for inheritance safety

# ---

### One-line summary

#Underscores in Python signal **intent and behavior**, not access control—ranging from “internal use” to “Python-managed special methods.”

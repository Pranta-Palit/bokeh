from bokeh.io import show
from bokeh.models import CustomJS, MultiSelect

multi_select = MultiSelect(title="Option:", value=["foo", "quux"],
                           options=[("foo", "Foo"), ("bar", "BAR"), ("baz", "bAz"), ("quux", "quux")])
multi_select.js_on_change("value", CustomJS(code="""
    console.log('multi_select: active=' + this.value, this.toString())
"""))

show(multi_select)

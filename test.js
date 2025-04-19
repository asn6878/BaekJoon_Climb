var __esDecorate = (this && this.__esDecorate) || function (ctor, descriptorIn, decorators, contextIn, initializers, extraInitializers) {
    function accept(f) { if (f !== void 0 && typeof f !== "function") throw new TypeError("Function expected"); return f; }
    var kind = contextIn.kind, key = kind === "getter" ? "get" : kind === "setter" ? "set" : "value";
    var target = !descriptorIn && ctor ? contextIn["static"] ? ctor : ctor.prototype : null;
    var descriptor = descriptorIn || (target ? Object.getOwnPropertyDescriptor(target, contextIn.name) : {});
    var _, done = false;
    for (var i = decorators.length - 1; i >= 0; i--) {
        var context = {};
        for (var p in contextIn) context[p] = p === "access" ? {} : contextIn[p];
        for (var p in contextIn.access) context.access[p] = contextIn.access[p];
        context.addInitializer = function (f) { if (done) throw new TypeError("Cannot add initializers after decoration has completed"); extraInitializers.push(accept(f || null)); };
        var result = (0, decorators[i])(kind === "accessor" ? { get: descriptor.get, set: descriptor.set } : descriptor[key], context);
        if (kind === "accessor") {
            if (result === void 0) continue;
            if (result === null || typeof result !== "object") throw new TypeError("Object expected");
            if (_ = accept(result.get)) descriptor.get = _;
            if (_ = accept(result.set)) descriptor.set = _;
            if (_ = accept(result.init)) initializers.unshift(_);
        }
        else if (_ = accept(result)) {
            if (kind === "field") initializers.unshift(_);
            else descriptor[key] = _;
        }
    }
    if (target) Object.defineProperty(target, contextIn.name, descriptor);
    done = true;
};
var __runInitializers = (this && this.__runInitializers) || function (thisArg, initializers, value) {
    var useValue = arguments.length > 2;
    for (var i = 0; i < initializers.length; i++) {
        value = useValue ? initializers[i].call(thisArg, value) : initializers[i].call(thisArg);
    }
    return useValue ? value : void 0;
};
function readonly(writable) {
    return function (target, decoratedPropertyName) {
        return {
            writable: !writable,
        };
    };
}
var Test = function () {
    var _a;
    var _data1_decorators;
    var _data1_initializers = [];
    var _data1_extraInitializers = [];
    var _data2_decorators;
    var _data2_initializers = [];
    var _data2_extraInitializers = [];
    return _a = /** @class */ (function () {
            function Test() {
                this.property = 'property';
                this.data1 = __runInitializers(this, _data1_initializers, 0);
                this.data2 = (__runInitializers(this, _data1_extraInitializers), __runInitializers(this, _data2_initializers, 0));
                __runInitializers(this, _data2_extraInitializers);
            }
            return Test;
        }()),
        (function () {
            var _metadata = typeof Symbol === "function" && Symbol.metadata ? Object.create(null) : void 0;
            _data1_decorators = [readonly(false)];
            _data2_decorators = [readonly(true)];
            __esDecorate(null, null, _data1_decorators, { kind: "field", name: "data1", static: false, private: false, access: { has: function (obj) { return "data1" in obj; }, get: function (obj) { return obj.data1; }, set: function (obj, value) { obj.data1 = value; } }, metadata: _metadata }, _data1_initializers, _data1_extraInitializers);
            __esDecorate(null, null, _data2_decorators, { kind: "field", name: "data2", static: false, private: false, access: { has: function (obj) { return "data2" in obj; }, get: function (obj) { return obj.data2; }, set: function (obj, value) { obj.data2 = value; } }, metadata: _metadata }, _data2_initializers, _data2_extraInitializers);
            if (_metadata) Object.defineProperty(_a, Symbol.metadata, { enumerable: true, configurable: true, writable: true, value: _metadata });
        })(),
        _a;
}();
var t = new Test();
t.data1 = 1000;
t.data2 = 1000; // 런타임 에러 !! - data2는 writable이 false라서 값을 대입할 수가 없다.

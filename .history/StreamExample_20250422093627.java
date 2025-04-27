// 方案一：使用filter和map的组合
List<StockTimeRange> result1 = rule.getMultiRuleInfoList().stream()
        .filter(item -> item.getStockTimeRange() != null)
        .map(MultiRuleInfo::getStockTimeRange)
        .collect(Collectors.toList());

// 方案二：使用map和filter的组合
List<StockTimeRange> result2 = rule.getMultiRuleInfoList().stream()
        .map(MultiRuleInfo::getStockTimeRange)
        .filter(Objects::nonNull)
        .collect(Collectors.toList());

// 如果需要同时过滤掉空字符串（假设StockTimeRange是String类型）
List<String> result3 = rule.getMultiRuleInfoList().stream()
        .map(MultiRuleInfo::getStockTimeRange)
        .filter(timeRange -> timeRange != null && !timeRange.trim().isEmpty())
        .collect(Collectors.toList()); 
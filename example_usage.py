from client import MultiModelCostLatencyPricePerformanceRouterClient

def main():
    client = MultiModelCostLatencyPricePerformanceRouterClient()
    res = client.route_optimal_model(4500, 400)
    print(f"Selected Endpoint: {res['selected_model_endpoint']}")
    print(f"Estimated Cost: ${res['estimated_cost_usd']}")
    print(f"Cost Savings: {res['cost_savings_pct']}%")

if __name__ == "__main__":
    main()

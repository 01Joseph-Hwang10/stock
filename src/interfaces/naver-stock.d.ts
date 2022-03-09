/**
 * # Naver stock API References
 * 
 * unknown type means literally unknown, needs research of the type
 */

// Endpoint : GET https://m.stock.naver.com/api/stock/<itemCode:string>/integration

// JSON Response

/**
 * Utility type. Makes given type nullable.
 */
type Nullable<T = any> = T | null | undefined;

/**
 * Response Array is given at this descending order of keys.
 */
type StockInfoKey =
    | '전일'
    | '시가'
    | '고가'
    | '저가'
    | '거래량'
    | '대금'
    | '시총'
    | '외인소진율'
    | '52주 최고'
    | '52주 최저'
    | 'PER'
    | 'EPS'
    | '추정PER'
    | '추정EPS'
    | 'PBR'
    | 'BPS'
    | '배당수익률'
    | '주식배당금';

interface StockInfo {
    code: string;
    key: StockInfoKey;
    value: string; // Comma seperated number with type of string
    compareToPreviousPrice?: {
        code: string;
        text: string;
        name: string;
    }
}

interface DetailedStockInfo {
    stockEndType: string;
    itemCode: string;
    reutersCode: string;
    stockName: string;
    totalInfos: StockInfo[];
    valueDesc?: string; // Date like
    valueAsc?: string; // Date like
    description?: Nullable<string>;
    dealTrendInfos: unknown[];
    researches: unknown[];
    industryCode: string; // Number like
    industryCompareInfo: unknown[];
    consensusInfo: Record<string, unknown>;
    shareholdersMeetingInfo: Record<string, unknown>;
    irScheduleInfo: Nullable<string>;
}

// Endpoint : GET https://m.stock.naver.com/api/stock/<itemCode:string>/basic

// JSON Response

interface BasicStockInfo {
    stockEndType: string;
    itemCode: string;
    reutersCode: string;
    stockName: string;
    sosok: string;
    closePrice: string;
    compareToPreviousClosePrice: string;
    compareToPreviousPrice: {
        code: string;
        text: string;
        name: string;
    },
    fluctuationsRatio: string;
    marketStatus: string;
    tradeStopType: {
        code: string;
        text: string;
        name: string;
    },
    stockExchangeType: {
        code: string;
        zoneId: string;
        nationType: string;
        delayTime: string;
        startTime: string;
        endTime: string;
        closePriceSendTime: string;
        nameKor: string;
        nameEng: string;
        name: string;
    },
    stockExchangeName: string;
    scriptChartTypes: string[];
    delayTime: string;
    delayTimeName: string;
    localTradeAt: string; // Date like
    imageCharts: Record<string, string>;
    endUrl: string;
    chartIqEndUrl: string;
}
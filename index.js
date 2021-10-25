// Knapsack
function max(a, b) {
    return (a > b) ? a : b;
}

function knapSack(W, wt, val, n) {
    let i, w;

    let K = new Array(n + 1);

    for (i = 0; i <= n; i++) {
        K[i] = new Array(W + 1);

        for (w = 0; w <= W; w++) {
            if (i == 0 || w == 0)
                K[i][w] = 0;

            else if (wt[i - 1] <= w) 
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);

            else
                K[i][w] = K[i - 1][w];

        }

    }

    return K[n][W];

}

let val = [ 60, 100, 120 ];
let wt = [ 10, 20, 30 ];
let W = 50;
let n = val.length;

document.write(knapSack(W, wt, val, n));


// Dijkstra
function minDistance(dist,sptSet) {
    let min = Number.MAX_VALUE;

    let min_index = -1;

    for(let v = 0; v < V; v++) {

        if (sptSet[v] == false && dist[v] <= min) {
            min = dist[v];

            min_index = v;

        }

    }

    return min_index;
}

function printSolution(dist) {
    document.write("Vertex \t\t Distance from Source<br>");

    for(let i = 0; i < V; i++) {
        document.write(i + " \t\t " + dist[i] + "<br>");
    }
}

function dijkstra(graph, src) {
    let dist = new Array(V);

    let sptSet = new Array(V);

    for(let i = 0; i < V; i++) {
        dist[i] = Number.MAX_VALUE;

        sptSet[i] = false;
    }

    dist[src] = 0;

    for (let count = 0; count < V - 1; count++) {
        let u = minDistance(dist, sptSet);

        sptSet[u] = true;
 
        for(let v = 0; v < V; v++) {
            if (!sptSet[v] && graph[u][v] != 0 && dist[u] != Number.MAX_VALUE && dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }

        }

    }

    printSolution(dist);
}

// Driver code
let graph = [ [ 0, 4, 0, 0, 0, 0, 0, 8, 0 ],
            [ 4, 0, 8, 0, 0, 0, 0, 11, 0 ],
            [ 0, 8, 0, 7, 0, 4, 0, 0, 2 ],
            [ 0, 0, 7, 0, 9, 14, 0, 0, 0],
            [ 0, 0, 0, 9, 0, 10, 0, 0, 0 ],
            [ 0, 0, 4, 14, 10, 0, 2, 0, 0],
            [ 0, 0, 0, 0, 0, 2, 0, 1, 6 ],
            [ 8, 11, 0, 0, 0, 0, 1, 0, 7 ],
            [ 0, 0, 2, 0, 0, 0, 6, 7, 0 ] ]
            
dijkstra(graph, 0);

